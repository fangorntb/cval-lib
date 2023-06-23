from requests import Session

from src.handlers.abstract_handler import AbstractHandler
from src.models.result import ResultResponse


class Result(AbstractHandler):
    def __init__(
            self,
            session: Session,
    ):
        self.route = f'http://127.0.0.1:9940/api/result'
        super().__init__(session)

    def get_result(self, result_id: str) -> ResultResponse:
        """
        :param result_id: id of result
        :return: ResultResponse
        """
        self._get(self.route + f'/{result_id}')
        return ResultResponse.parse_obj(self.send().json())

    def get_results(self, limit=100):
        """
        :param limit: limit of returned objects
        :return:
        """
        self._get(self.route + 's', params={'limit': limit})
        return [ResultResponse.parse_obj(i) for i in self.send().json()]
