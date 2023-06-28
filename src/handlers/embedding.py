from typing import List
from requests import Session, Response

from src.configs.main_config import MainConfig
from src.handlers.abstract_handler import AbstractHandler
from src.models.embedding import ImageEmbeddingModel


class Embedding(AbstractHandler):
    """
    Embeddings are vector representations of images
    obtained using pytorch or any other library
    """
    def __init__(
            self,
            session: Session,
            dataset_id: str = None,
            type_of_dataset: str = None,
            _is_not_second=True
    ):
        if _is_not_second and dataset_id is None:
            raise ValueError('dataset_id must be not None')
        if _is_not_second and type_of_dataset is None:
            raise ValueError('type_of_dataset must be not None')

        self.route = f'{MainConfig().main_url}/dataset/{dataset_id}/{type_of_dataset}/'
        super().__init__(session)

    def monkey_patch_url(self, dataset_id: str, type_of_dataset: str, ) -> None:
        self.route = f'{MainConfig().main_url}/dataset/{dataset_id}/{type_of_dataset}/'
        return self

    def get_many(self, start_limit: int = 0, stop_limit: int = 1000) -> ImageEmbeddingModel:
        """
        :param start_limit: upper limit of items
        :param stop_limit: lower limit of items
        :return: List[ImageEmbeddingModel]
        """
        self._get(self.route + '/embeddings', params={'start_limit': start_limit, 'stop_limit': stop_limit})
        return [ImageEmbeddingModel.parse_obj(i) for i in self.send().json()]

    def get_by_id(self, embedding_id: str, ) -> ImageEmbeddingModel:
        """
        :param embedding_id: id of embedding
        :return: ImageEmbeddingModel
        """
        self._get(self.route + f'/embedding/{embedding_id}')
        return [ImageEmbeddingModel.parse_obj(i) for i in self.send().json()]

    def upload_many(self, embeddings: List[ImageEmbeddingModel]) -> Response:
        """
        :param embeddings: List[ImageEmbeddingModel]
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._post(self.route + f'/embeddings', json=[i.dict() for i in embeddings])
        return self.send()

    def upload_by_id(self, embedding_id: str, embedding: ImageEmbeddingModel) -> Response:
        """
        :param embedding: List[ImageEmbeddingModel]
        :param embedding_id: id of embedding
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._post(self.route + f'/embedding/{embedding_id}', json=embedding.dict())
        return self.send()

    def update_many(self, embeddings: List[ImageEmbeddingModel]) -> Response:
        """
        :param embeddings: List[ImageEmbeddingModel]
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._put(self.route + f'/embeddings', json=[i.dict() for i in embeddings])
        return self.send()

    def update_by_id(self, embedding_id: str, embedding: ImageEmbeddingModel) -> Response:
        """
        :param embedding: List[ImageEmbeddingModel]
        :param embedding_id: id of embedding
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._put(self.route + f'/embedding/{embedding_id}', json=embedding.dict())
        return self.send()

    def delete_all(self) -> Response:
        """
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._delete(self.route + f'/embeddings')
        return self.send()

    def delete_by_id(self, embedding_id: str) -> Response:
        """
        :param embedding_id: id of embedding
        :return: Response, This method does not return anything useful to use, but performs an action
        """
        self._delete(self.route + f'/embedding/{embedding_id}')
        return self.send()
