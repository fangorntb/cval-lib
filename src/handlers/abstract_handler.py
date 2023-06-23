from requests import Request, Session, Response


class AbstractHandler(Request):
    def __init__(self, session: Session, sub: str = '', url=''):
        self.session = session
        self.sub = sub
        super().__init__(
            method=None,
            url=url,
            headers=session.headers,
            files=None,
            data=None,
            params=None,
            auth=None,
            cookies=None,
            hooks=None,
            json=None,
        )

    def _get(self, url: str, params=None):
        self.url = url
        self.method = 'get'
        self.params = params

    def _delete(self, url: str, params=None):
        self._get(url, params=params)
        self.method = 'delete'

    def _post(self, url: str, json=None, params=None):
        self._get(url, params=params)
        self.method = 'post'
        self.json = json

    def _put(self, url: str, json=None, params=None):
        self._post(url, json, params)
        self.method = 'put'

    @staticmethod
    def validate_response(resp: Response):
        if resp.status_code >= 400:
            raise Exception(resp.json() if resp.status_code != 500 else 'Internal Server Error :(')

    def send(self):
        resp = self.session.send(self.prepare())
        self.validate_response(resp)
        return resp
