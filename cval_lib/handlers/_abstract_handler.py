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