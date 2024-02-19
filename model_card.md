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
- **Model type:** Linear regression
- **Language(s) (NLP):** Not applicable
- **License:** [Apache 2](LICENSE)
- **Finetuned from model:** Not applicable

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** [this repository](../)
- **Paper:** Not yet applicable
- **Demo:** Not yet applicable

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->


### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->


### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->


## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

The code of this federated learning model will be provided in this repository. The execution will be using the Jupyter Notebook available in this repository, on a running and configured instance of [Vantage6](https://vantage6.ai).


## Training Details

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
