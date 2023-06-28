"""
Introducing CVAL Rest API, a powerful tool for AI developers in the computer vision field.
Our service combines the concepts of human-in-the-loop and active learning to improve the quality of
your models and minimize annotation costs for classification, detection, and segmentation cases.

With CVAL, you can iteratively improve your models by following our active learning loop.
First, manually or semi-automatically annotate a random set of images.
Next, train your model and use uncertainty and diversity methods to score the remaining images for annotation.
Then, manually or semi-automatically annotate the images marked as more confident to increase the accuracy of the model.
Repeat this process until you achieve an acceptable quality of the model.

Our service makes it easy to implement this workflow and improve your models quickly and efficiently.
Try our demo notebook to see how CVAL can revolutionize your computer vision projects.

To obtain a client_api_key, please send a request to k.suhorukov@digital-quarters.com
"""

from pydantic import BaseModel, Field


class DatasetModel(BaseModel):
    """
    :param dataset_name: the name of dataset
    :param dataset_description: the description of dataset
    :raises pydantic.error_wrappers.ValidationError:
    if len(dataset_name) > 32 or len(dataset_description) > 256
    """
    dataset_name: str | None = Field(max_length=32,)
    dataset_description: str | None = Field(max_length=256,)


class DatasetDefaultResponse(BaseModel):
    """
    :param dataset_id: id of dataset
    """
    dataset_id: str


class DatasetResponse(DatasetModel):
    """
    :param dataset_id: id of dataset
    :param dataset_name: the name of dataset
    :param dataset_description: the description of dataset
    :raises pydantic.error_wrappers.ValidationError:
    if len(dataset_name) > 32 or len(dataset_description) > 256
    """
    dataset_id: str