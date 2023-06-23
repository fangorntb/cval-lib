from typing import List
from pydantic import validator

from pydantic import BaseModel, Field


class BBoxScores(BaseModel):
    """
    :param category_id: id of the category in FramePrediction namespace
    :param score: prediction of model on that bbox
    """
    category_id: str
    score: float


class FramePrediction(BaseModel):
    """
    :param frame_id: id of the frame
    :param predictions: bbox scores
    """
    frame_id: str = Field(max_length=32)
    predictions: List[BBoxScores]


class DetectionSamplingOnPremice(BaseModel):
    """
    :param num_of_samples: absolute number of samples to select
    :param bbox_selection_policy:
    Which bounding box to select when there are multiple boxes on an image,
    according to their confidence. Currently supports: min, max, mean
    :selection_strategy: Currently supports: margin, least, ratio, entropy
    :param frames: prediction for th picture and the bbox
    :type frames: List[FramePrediction]
    :raises ValueError if value not in allowed
    """
    num_of_samples: int
    bbox_selection_policy: str
    selection_strategy: str
    sort_strategy: str
    frames: List[FramePrediction] = Field(max_items=10_000)

    @validator('bbox_selection_policy')
    def validate_bbox_selection_policy(cls, value):
        allowed = ['min', 'max', 'sum', 'mean']
        if value not in allowed:
            raise ValueError(f"allowed bbox_selection_policy = {allowed}")
        return value

    @validator('selection_strategy')
    def validate_selection_strategy(cls, value):
        allowed = 'margin,least,ratio,entropy,probability'.split(',')
        if value not in allowed:
            raise ValueError(f"allowed selection_strategy = {allowed}")
        return value

    @validator('sort_strategy')
    def validate_sort_strategy(cls, value):
        allowed = 'max,min'.split(',')
        if value not in allowed:
            raise ValueError(f"allowed sort_strategy = {allowed}")
        return value
