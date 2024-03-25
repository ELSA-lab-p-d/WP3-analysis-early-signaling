<!-- 
# For reference on model card metadata, see the spec: https://github.com/huggingface/hub-docs/blob/main/modelcard.md?plain=1
# Doc / guide: https://huggingface.co/docs/hub/model-cards
-->

# Model Card for Analysis early signaling insights

<!-- Provide a quick summary of what the model is/does. -->

This model provides insights into the effectiveness of early signaling in debt signals at local municipalities in The Netherlands. Effectiveness is measured as a reduction of signals after the municipality succesfully contacted the subject.

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** Johan van Soest
- **Funded by:** Ministry of the Interior and Kingdom Relations
- **Shared by:** Johan van Soest
- **Model type:** to be determined (e.g. logistic regression or decision tree)
- **Language(s) (NLP):** Not applicable
- **License:** [Apache 2](LICENSE)
- **Finetuned from model:** Not applicable

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [this repository](../)
- **Paper:** Not yet applicable
- **Demo:** [http://server-ui.wp3.johanvansoest.nl/](http://server-ui.wp3.johanvansoest.nl/)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->
The model is developed to gain insights into predictors for effective early signaling late payments. These insights can be used to set filters / alerts which correspond to actions taken by municipalities. Hence the outcome is **not** a prediction model which can be used directly and only gives insights into the filters settings municipalities can use.

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
As mentioned above, the model should not be used without human oversight. This model is not fine-tuned to be readily used in production environments. Insights gained by this analysis will result into an evaluation by municipalities whether or not to change their filters.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
This model should not be used for the following scenario's:

- Automated decision making with respect to contacting citizens yes/no
- Other purposes such as predicting which individuals have a high chance of debt for malicious use cases
- Excluding model users (e.g. municipalities) from legal obligations or denying services based on the model output
- Citizens to claim (based on the model output) that they have the legal right of financial support
- Boosting key performance indicators (KPIs) at municipalities regarding the offered and accepted help

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->
The insights are specifically developed to detect people at risk of problematic debt, and to determine what kind of help should be offered. Hence, the development *intent* is to *help* citizens. The data developed to train this model is based on routine data/information available at muncipalities, including the biases this data entails. For example, the current signaling is based on rent, drinking water, energy providers and healthcare insurance (see [here](https://www.rijksoverheid.nl/onderwerpen/schulden/gemeenten-sneller-signaleren-van-schulden), in Dutch). Hence, the subgroup which can be detected, and for which the recommendations are given, are citizens where this information is being recorded. Some subgroups (e.g. young adults) might be excluded as information is not (yet) available.

Since the model is trained to *help* citizens, the model cannot be used for control and monitoring purposes (e.g. detecting fraud).

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

When using the learned insights, and applying them to set different filters at municipalities, carefull monitoring needs to be considered to determine whether specific sub-groups are not reached anymore. Furthermore, the implementation of data-driven insights leads to bias and effects in outcome measurement. Post-implementation monitoring is warranted to evaluate whether the insights lead to the intended outcome (better and more effective early signaling of debt).

<!-- ## How to Get Started with the Model -->

## Training Details

Legal agreements to setup the consortium and infrastructure to perform the analysis are available in the [legal templates](./legal_templates/) folder.

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]


#### Training Hyperparameters

- **Training regime:** {{ training_regime | default("[More Information Needed]", true)}} <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->


#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->


#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->


### Results


#### Summary


## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->


## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** {{ hardware_type | default("[More Information Needed]", true)}}
- **Hours used:** {{ hours_used | default("[More Information Needed]", true)}}
- **Cloud Provider:** {{ cloud_provider | default("[More Information Needed]", true)}}
- **Compute Region:** {{ cloud_region | default("[More Information Needed]", true)}}
- **Carbon Emitted:** {{ co2_emitted | default("[More Information Needed]", true)}}

## Technical Specifications [optional]

### Model Architecture and Objective

### Compute Infrastructure

#### Hardware


#### Software

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

**APA:**


## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

## More Information [optional]


## Model Card Authors [optional]

- Johan van Soest

## Model Card Contact

- Johan van Soest (j.vansoest@maastrichtuniversity.nl)
