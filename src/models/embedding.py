from typing import List

from pydantic import BaseModel, Field


class ImageEmbeddingModel(BaseModel):
    """
    Describes the embedding model
    :param id: id of embedding
    :type id: str
    :param image_embedding: image embedding vector
    :type image_embedding: List[float]
    """
    id: str = Field(max_length=32)
    image_embedding: List[float]

