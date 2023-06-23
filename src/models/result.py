from pydantic import BaseModel


class WeightsConfigResponse(BaseModel):
    """
    :param weights_id: id of weights
    :param retrain_model: use model retrain
    :param old_weights_version: previous weights version
    :param new_weights_version: current weights version
    """
    weights_id: str
    retrain_model: bool
    old_weights_version: str
    new_weights_version: str


class WeightsSimpleResponse(BaseModel):
    """
    :param weights_id: id of weights
    :param version: current weights version
    """
    weights_id: str | None
    version: str | None


class ResultResponse(BaseModel):
    """
    :param result_id: id of result for polling
    :param dataset_id: id of dataset
    :param time_start: starting unix timestamp
    :param time_end: ending unix timestamp
    :param type_of_task: type of task: detection, classification
    :param action: action of result: sampling or test
    :param weights: weights of result
    """
    result_id: str
    dataset_id: str
    time_start: float
    time_end: float | None
    type_of_task: str
    action: str
    weights: WeightsConfigResponse | None
