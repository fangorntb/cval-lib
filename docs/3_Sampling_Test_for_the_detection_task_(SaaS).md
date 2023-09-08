# Sampling for the detection task (SaaS) & Test

[Colab demo](https://colab.research.google.com/drive/1Ex6ghcrd2fj1sxImiItbzcN8RhTJ3EfT#scrollTo=laajBVirvRSV)

## Sampling
### Parameter Description

#### dataset_id

id of the dataset into which the annotations and images were uploaded.

To work in the pipeline of active learning not according to the on-premise scheme, 
you need to create a dataset and upload to its training, test, validation parts of
the picture and annotations for pictures test, validation and initial (random) train
annotations for pictures.

#### num_samples

Number of samples requested by the customer from the set of unlabelled images.

#### weights_of_model

parameters for loading model weights that were obtained in the previous iteration.
- weights_id: unique identifier of the model weights
- retrain_model: perform a model retrain
- weights_version: weights Version to be used in the operation

#### model

type of the model. Currently, supports: b0, resnet50, mobilenet

#### selection_strategy

##### Entropy Methods
this is a set of methods for identifying unmarked elements
near the decision boundary in your current machine learning model.
* least: the least confidence sampling is the difference between the most reliable forecast and 100% confidence.
* margin: the difference between the two most reliable predictions
* ratio: the ratio between the two most confident forecasts
* entropy: the difference between all predictions, as defined in information theory.
##### Diversity Methods
This method aims to select examples that are as diverse as possible and cover different aspects of the data. This helps prevent the model from being retrained on certain types of examples.

* ...

#### batch_unlabeled

the limit of unlabeled samples that can be processed

#### bbox_selection_policy

This parameter specifies how AL score will be aggregated if multiple predictions have been submitted for an image. It can take the following values:
* min - the minimum AL score for the image will be selected;
* max - the maximum AL score for the image will be selected; 
* sum - all AL scores for the image will be summed up;
* mean - average AL score for the image will be calculated.

#### bbox_selection_quantile_range
in what range of confidence will the bbox selection policy be applied.

## Test

To perform the model test, select your weights and model.