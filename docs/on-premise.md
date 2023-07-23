# Sampling for the detection task (on-premise)
## Parameter Description

### num_samples

**Number of samples** requested by the customer from the set of unlabelled images.

### frames

Set of **unlabelled images**. Each image has a required parameter frame_id and an optional parameter predictions.
### predictions

The model's **predictions for an image**. Each prediction has an optional category_id, score and embedding_id parameter. Predictions are optional for an image. 
_If the request does not have a prediction for an image, the image will have a **fake prediction**._

### category_id

The label class that has been assigned by the model for this prediction.
_This parameter is optional._ 

### score

The confidence with which the model made the prediction (float, from 0 to 1). This parameter is optional. 

### embedding_id
Embedding ID for prediction.  This parameter is optional and is only used for diversity-based strategies. The embedding must first be loaded into the service using the client library's embedding methods.
> Fake prediction
In case of fake predictions for margin, least, ratio, entropy methods the service will assign score = 0,5. For the probability method, the service will set score = 0. 

> For fake predictions in diversity methods, the service will set score = 1 and category_id different from target (e.g., if target categories are "1", "2", "3", the service will assign category "-1"). 

> The client should take care of generating the embedding for the fake prediction himself. In this case it is recommended to generate embedding for the whole image.

### selection_strategy

This parameter defines the sampling strategy and can take the following values: margin, least, ratio, entropy, probability, clustering. The margin, least, ratio, entropy strategies belong to the group of strategies based on uncertainty. Clustering is a diversity strategy.
Strategies based on uncertainty
Based on the confidence of the model predictions (score) for each image, the service determines an Active Learning Score (al_score) by which the images are ranked.

> Calculation of al_score for margin, least, ratio, entropy is performed by the following formulas: 
> [Uncertainty Sampling Cheatsheet](https://robertmunro.com/Uncertainty_Sampling_Cheatsheet_PyTorch.pdf)

### In brief:
* **least** - difference between the most confident prediction and 100% confidence;
* **margin** - difference between the top two most confident predictions;
* **ratio**  - ratio between the top two most confident predictions;
* **entropy** - difference between all predictions, as defined by information theory.

For a **probability** strategy al_score is always equal to the score value.

> Currently the service only supports single class predictions, so for the purpose of calculating al_score the service uses the following logic: score1 = score, score2 = (1 - score).

For uncertainty strategies, two more parameters bbox_selection_policy and sort_strategy need to be set.
Diversity-based strategies (under construction).
> Currently, one diversity strategy is supported -- **clustering**. Based on embeddings of predictions, their classes and confidence, clusters of images are constructed. Centroids are selected from the clusters. The centroids will be selected as the most diverse images. 

An example of embedding extraction and **clustering-based** sampling is presented in the demo notebook (link). #TODO

### bbox_selection_policy

This parameter specifies how al_score will be aggregated if multiple predictions have been submitted for an image. It can take the following values:
* **min** - the **minimum** score for the image will be selected;
* **max** - the **maximum** score for the image will be selected; 
* **sum** - all **scores** for the image will be summed up;
* **mean** - **average** score for the image will be calculated.

### sort_strategy

This parameter defines in what **order the images will be sorted** by al_score value and can take the following values: ascending, descending.

If ascending is selected, the images will be sorted in **ascending order**. Descending - in descending order.
After sorting is applied, images will always be selected **from the left**. For example, if descending sorting is selected, then images with **maximum score** values will be selected.

### Selection Strategy Combination (under construction)
> A typical combination of sampling strategies is to sequentially select a larger number of samples using the uncertainty strategy and then apply the diversity strategy to this set. To simplify the construction of this pipeline, the service allows you to specify a result_id parameter, which will pass all output values from the previous sampling step to the method.

See example request:

TODO: Insert code example ()


