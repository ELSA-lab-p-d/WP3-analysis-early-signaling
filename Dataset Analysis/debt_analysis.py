
import pandas as pd
import logging

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

def accumulate_debt_by_matched_postcode(data, postcode_column, debt_column):
    """
    Sum the debt amounts for matched postcodes using the corrected data.
    """
    logging.info(f"Accumulating debt by postcode for {postcode_column}...")
    grouped_data = data.groupby(postcode_column).agg(
        Total_Debt=pd.NamedAgg(column=debt_column, aggfunc='sum'),
        Individual_Debts=pd.NamedAgg(column=debt_column, aggfunc=list),  # Collect all debts as a list
        Count=pd.NamedAgg(column=postcode_column, aggfunc='size')
    ).reset_index()

    logging.info("Grouping complete. Calculated total debts and counts.")
    
    matched_postcodes = grouped_data[grouped_data['Count'] > 1]
    logging.info(f"Found {matched_postcodes.shape[0]} matched postcodes with multiple entries.")
    
    return matched_postcodes

def print_formatted_results(data, postcode_column, total_debt_column):
    """
    Print the results in a formatted string, including individual debt values.
    """
    for _, row in data.iterrows():
        individual_debts = ', '.join([f"{amount:,.2f}" for amount in row['Individual_Debts']])
        print(f"This postcode, {row[postcode_column]}, has {row['Count']} entries with individual debts of {individual_debts}, "
              f"and the total amount of debt is: {row[total_debt_column]:,.2f}")

file_path = '/bi_export_12299_ XXLLNC.xlsx'
data = load_data(file_path)
postcode_column = 'RIS Matching: Postcode (4)'
debt_column = 'RIS Matching: Achterstandsbedrag'
matched_debt_summary = accumulate_debt_by_matched_postcode(data, postcode_column, debt_column)

print_formatted_results(matched_debt_summary, postcode_column, 'Total_Debt')
