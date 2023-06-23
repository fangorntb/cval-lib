from typing import List

from requests import Session

from src.configs.main_config import MainConfig
from src.handlers.abstract_handler import AbstractHandler
from src.handlers.detection import Detection
from src.handlers.embedding import Embedding
from src.handlers.result import Result
from src.models.dataset import DatasetModel, DatasetResponse


class Dataset(AbstractHandler):
    def __init__(self, session: Session):
        self.dataset_request = DatasetModel
        self.route = f'{MainConfig().main_url}/dataset'
        self.dataset_id = None
        self.result = Result(session)
        self.embedding = Embedding(session, _is_not_second=False).monkey_patch_url
        self.detection = Detection(session)
        super().__init__(session)

    def __repr__(self):
        return f'<dataset {self.dataset_id}>'

    def _construct_request(self, name: str, description: str):
        self.dataset_request = DatasetModel
        if name is not None:
            self.dataset_request.dataset_name = name
        if description is not None:
            self.dataset_request.dataset_description = description

    def create(
            self,
            name: str = None,
            description: str = None,
    ) -> str:
        """
        this method creates a dataset
        :param name: the name of dataset
        :param description: the name of dataset
        :return: id of dataset (dataset_id)
        """
        self._construct_request(name, description)
        self._post(url=self.route, json=self.dataset_request().dict())
        self.dataset_id = self.send().json().get('dataset_id')
        return self.dataset_id

    def update(
            self,
            dataset_id: str = None,
            name: str = None,
            description: str = None,
    ) -> DatasetResponse:
        """
        this method updates a dataset
        :param dataset_id: id of dataset
        :param name: the name of dataset
        :param description: the description of dataset
        :return: DatasetResponse model with updates
        """
        dataset_id = self.set_dataset_id(dataset_id)
        self._construct_request(name, description)
        self.dataset_request.dataset_id = dataset_id
        self._put(url=self.route+f'/{dataset_id}', json=self.dataset_request().dict(), )
        self.dataset_request = DatasetModel.parse_obj(self.send().json())
        return self.dataset_request

    def set_dataset_id(self, dataset_id: str = None):
        if dataset_id is None:
            dataset_id = self.dataset_id
        self.dataset_id = dataset_id
        if self.dataset_id is None:
            raise ValueError('dataset_id cannot be None')
        return self.dataset_id

    def get(
            self,
            dataset_id: str = None,
    ) -> DatasetResponse:
        """
        this method returns a dataset name and description by dataset_id
        :param dataset_id: id of dataset
        :return: DatasetResponse model with updates
        """
        dataset_id = self.set_dataset_id(dataset_id)
        self._get(url=self.route+f'/{dataset_id}')
        return DatasetModel.parse_obj(self.send().json())

    def get_all(
            self,
            name: str = None,
            description: str = None,
    ) -> List[DatasetResponse]:
        """
        this method returns a dataset name and description by dataset_id
        :param name: the name of dataset. regexp
        :param description: the description of dataset. regexp
        :return: DatasetResponse model with updates
        """
        self._construct_request(name, description)
        self._get(url=self.route+'s/all', params=self.dataset_request().dict())
        return [DatasetResponse.parse_obj(i) for i in self.send().json()]
