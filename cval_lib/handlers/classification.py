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

from cval_lib.handlers._based_on_json import BasedOnJSON
from cval_lib.models.classification import (
    ClassificationTest,
    ClassificationSampling,
)
from cval_lib.models.result import ResultResponse


class Classification(BasedOnJSON):
    def saas_sampling(self, dataset_id, config: ClassificationSampling) -> ResultResponse:
        """
        Start Active Learning selection for a specific dataset ID.
        """
        return self.__processing__(
            f'/dataset/{dataset_id}/sampling/classification',
            self._post,
            ResultResponse,
            config,
        )

    def saas_test(self, dataset_id: str, config: ClassificationTest) -> ResultResponse:
        """
        Start model test for a specific dataset ID.
        """
        return self.__processing__(
            f'/dataset/{dataset_id}/test/classification',
            self._post,
            ResultResponse,
            config,
        )
