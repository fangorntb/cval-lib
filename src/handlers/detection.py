from requests import Session

from src.configs.main_config import MainConfig
from src.handlers.abstract_handler import AbstractHandler
from src.handlers.result import Result
from src.models.models import DetectionSamplingOnPremice


class Detection(AbstractHandler):
    def __init__(
            self,
            session: Session,
    ):
        self.route = f'{MainConfig().main_url}'
        self.result = Result(session)
        super().__init__(session)

    def sampling(self, config: DetectionSamplingOnPremice) -> str:
        """
        :param config: request model
        :return: result_id
        """
        return self.session.send(
            self._post(self.route + 'on-premice/sampling/detection', json=config.dict()),
        ).json().get('result_id')
