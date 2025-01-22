import pandas as pd
import logging
import textwrap

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load the Excel file into a DataFrame and prepare the debt column.
    """
    logging.info("Loading data...")
    data = pd.read_excel(file_path)
    logging.info(f"Data loaded with {data.shape[0]} rows and {data.shape[1]} columns.")
    
    data['RIS Matching: Achterstandsbedrag'] = data['RIS Matching: Achterstandsbedrag'].str.replace(',', '').astype(float)
    logging.info("Converted 'RIS Matching: Achterstandsbedrag' to numeric format.")
    
    return data

def categorize_debt(debt_amount):
    if debt_amount < 50000:
        return 'Low'
    elif 50000 <= debt_amount < 150000:
        return 'Medium'
    else:
        return 'High'



def accumulate_debt_by_matched_postcode(data, postcode_column, debt_column):
    logging.info(f"Accumulating debt by postcode for {postcode_column}...")
    grouped_data = data.groupby(postcode_column).agg(
        Total_Debt=pd.NamedAgg(column=debt_column, aggfunc='sum'),
        Individual_Debts=pd.NamedAgg(column=debt_column, aggfunc=list),
        Count=pd.NamedAgg(column=postcode_column, aggfunc='size'),
        Actions=pd.NamedAgg(column='Bakje', aggfunc=lambda x: x.value_counts().to_dict()),
        Debt_Categories=pd.NamedAgg(column=debt_column, aggfunc=lambda x: x.apply(categorize_debt).value_counts().to_dict())
    ).reset_index()
    return grouped_data

def profile_high_risk_postcodes(data, threshold):
    """
    Generate detailed profiles for high-risk postcodes.
    """
    high_risk = data[data['Total_Debt'] >= threshold]
    return high_risk

def print_formatted_results(data, postcode_column, total_debt_column):
    """
    Print formatted results for all postcodes and detailed profiles for high-risk postcodes.
    """
    for _, row in data.iterrows():
        individual_debts = ', '.join([f"{amount:,.2f}" for amount in row['Individual_Debts']])
        actions_summary = ', '.join([f"{action}: {count}" for action, count in row['Actions'].items()])
        debt_category_summary = ', '.join([f"{category}: {count}" for category, count in row['Debt_Categories'].items()])
        print(f"Postcode: {row[postcode_column]}\n"
              f"Entries: {row['Count']}\n"
              f"Individual Debts: {individual_debts}\n"
              f"Total Debt: {row[total_debt_column]:,.2f}\n"
              f"Actions Taken: {actions_summary}\n"
              f"Debt Categories: {debt_category_summary}\n"
              "----------------------------------------")
        


def plot_actions_frequency(data):
    actions = {}
    for idx, row in data.iterrows():
        for action, count in row['Actions'].items():
            if action in actions:
                actions[action] += count
            else:
                actions[action] = count

    wrapped_labels = ['\n'.join(textwrap.wrap(action, width=20)) for action in actions.keys()]
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(wrapped_labels, actions.values(), color='lightblue')
    ax.set_xlabel('Actions')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Actions Taken')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()
    fig.text(0.5, -0.05, 'This bar chart displays the frequency of actions taken across all postcodes.', 
             ha='center', fontsize=10)
    plt.show()

# Assuming this function is called with the appropriate data

def plot_debt_severity_distribution(data):
    debt_categories = {'Low': 0, 'Medium': 0, 'High': 0}
    for idx, row in data.iterrows():
        for category, count in row['Debt_Categories'].items():
            debt_categories[category] += count

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(debt_categories.values(), labels=debt_categories.keys(), autopct='%1.1f%%', 
           startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
    ax.set_title('Debt Severity Distribution')
    fig.text(0.5, -0.05, 'This pie chart shows the distribution of debt severity categories across all postcodes.', 
             ha='center', fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_total_debt_by_postcode(data, postcode_column, total_debt_column):
    fig, ax = plt.subplots(figsize=(12, 8))
    data.sort_values(by=total_debt_column, ascending=False, inplace=True)
    ax.bar(data[postcode_column], data[total_debt_column], color='skyblue')
    ax.set_xlabel('Postcode')
    ax.set_ylabel('Total Debt')
    ax.set_title('Total Debt by Postcode')
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.text(0.5, -0.05, 'This bar graph illustrates the total debt amounts aggregated by postcode.', 
             ha='center', fontsize=10)
    plt.show()


import numpy as np

def preprocess_recidive_columns(data, recidive_columns):
    """
    Preprocess Recidive columns to map 'Ja' to 1 and 'Nee' to 0,
    handling complex or unexpected strings gracefully.
    """
    for col in recidive_columns:
        data[col] = data[col].apply(lambda x: 1 if 'Ja' in str(x) else 0 if 'Nee' in str(x) else None)
    return data

def analyze_recidive_trends(data):
    """
    Perform numerical analysis on recidive data over six months.
    """
    recidive_columns = [
        'RIS Matching: Recidive maand-1',
        'RIS Matching: Recidive maand-2',
        'RIS Matching: Recidive maand-3',
        'RIS Matching: Recidive maand-4',
        'RIS Matching: Recidive maand-5',
        'RIS Matching: Recidive maand-6'
    ]
    
    # Total recidive counts
    total_recidive = data[recidive_columns].sum().sum()
    
    # Monthly recidive counts
    monthly_recidive = data[recidive_columns].sum()
    
    # Average recidive per month
    avg_recidive_per_month = monthly_recidive.mean()
    
    # Total recidive by postcode
    data['Total Recidive'] = data[recidive_columns].sum(axis=1)
    recidive_by_postcode = data.groupby('RIS Matching: Postcode (4)')['Total Recidive'].sum()

    analysis = {
        'Total Recidive': total_recidive,
        'Monthly Recidive': monthly_recidive.to_dict(),
        'Average Recidive Per Month': avg_recidive_per_month,
        'Recidive by Postcode': recidive_by_postcode.sort_values(ascending=False).to_dict()
    }
    
    return analysis

def plot_recidive_trend(data):
    """
    Plot the trend of recidive cases over six months.
    """
    recidive_columns = [
        'RIS Matching: Recidive maand-1',
        'RIS Matching: Recidive maand-2',
        'RIS Matching: Recidive maand-3',
        'RIS Matching: Recidive maand-4',
        'RIS Matching: Recidive maand-5',
        'RIS Matching: Recidive maand-6'
    ]
    
    monthly_recidive = data[recidive_columns].sum()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(monthly_recidive.index, monthly_recidive.values, marker='o', linestyle='-', color='blue')
    ax.set_xlabel('Months')
    ax.set_ylabel('Number of Recidive Cases')
    ax.set_title('Trend of Recidive Cases Over Six Months')
    plt.xticks(ticks=np.arange(len(recidive_columns)), labels=recidive_columns, rotation=45)
    plt.tight_layout()
    plt.show()

def plot_recidive_heatmap(data):
    """
    Plot a heatmap of recidive cases by postcode and month.
    """
    recidive_columns = [
        'RIS Matching: Recidive maand-1',
        'RIS Matching: Recidive maand-2',
        'RIS Matching: Recidive maand-3',
        'RIS Matching: Recidive maand-4',
        'RIS Matching: Recidive maand-5',
        'RIS Matching: Recidive maand-6'
    ]
    
    recidive_matrix = data.groupby('RIS Matching: Postcode (4)')[recidive_columns].sum()
    fig, ax = plt.subplots(figsize=(12, 8))
    cax = ax.matshow(recidive_matrix, cmap='Blues')
    plt.colorbar(cax)
    ax.set_xticks(np.arange(len(recidive_columns)))
    ax.set_xticklabels(recidive_columns, rotation=45)
    ax.set_yticks(np.arange(len(recidive_matrix.index)))
    ax.set_yticklabels(recidive_matrix.index)
    ax.set_title('Heatmap of Recidive Cases by Postcode and Month', pad=20)
    plt.tight_layout()
    plt.show()



file_path = '/content/bi_export_12299_ XXLLNC.xlsx'
data = load_data(file_path)
postcode_column = 'RIS Matching: Postcode (4)'
debt_column = 'RIS Matching: Achterstandsbedrag'
matched_debt_summary = accumulate_debt_by_matched_postcode(data, postcode_column, debt_column)

# Print all postcode results
print_formatted_results(matched_debt_summary, postcode_column, 'Total_Debt')

# Profile and print high-risk postcodes if needed
high_risk_threshold = 1000000  # Example threshold
high_risk_postcodes = profile_high_risk_postcodes(matched_debt_summary, high_risk_threshold)
if not high_risk_postcodes.empty:
    print("\nHigh-risk postcode profiles:")
    print_formatted_results(high_risk_postcodes, postcode_column, 'Total_Debt')


# Plotting actions frequency
plot_actions_frequency(matched_debt_summary)

# Plotting debt severity distribution
plot_debt_severity_distribution(matched_debt_summary)


# # Plotting total debt by postcode
# plot_total_debt_by_postcode(matched_debt_summary, postcode_column, 'Total_Debt')


recidive_columns = [
    'RIS Matching: Recidive maand-1',
    'RIS Matching: Recidive maand-2',
    'RIS Matching: Recidive maand-3',
    'RIS Matching: Recidive maand-4',
    'RIS Matching: Recidive maand-5',
    'RIS Matching: Recidive maand-6'
]


# Preprocess Recidive columns
data = preprocess_recidive_columns(data, recidive_columns)

# Analyze Recidive trends
recidive_analysis = analyze_recidive_trends(data)
print("Recidive Analysis:")
for key, value in recidive_analysis.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")

# Plot the trend of Recidive cases
plot_recidive_trend(data)

# Plot the heatmap of Recidive cases by postcode and month
# plot_recidive_heatmap(data)