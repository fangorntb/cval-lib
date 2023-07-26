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

from typing import List, Optional, Any, Union

from pydantic import BaseModel, Field


class EmbeddingModel(BaseModel):
    embedding_id: Optional[str]
    embedding: List[float]


class FrameEmbeddingModel(BaseModel):
    frame_id: str = Field(max_length=32)
    embeddings: List[EmbeddingModel]


class FrameEmbeddingResponseModel(BaseModel):
    frame_id: str
    embeddings_quantity: int
    embeddings: List[str]


class EmbeddingsMetaResponse(BaseModel):
    frames_quantity: int
    frames: Union[List[FrameEmbeddingResponseModel], List]
