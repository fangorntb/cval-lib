
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
