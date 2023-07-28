# Schemes of work with the service
Interaction with the service can be carried out according to two schemes:

* All in Service - when model training takes place at the service site, for this purpose the service must have access to the client's dataset.
* On-Premise - when the model and the dataset are on the client's side. Sampling is performed in the service based on model predictions and image embeddings (see Fig. 1).

[//]: # (Константин, пришлите .jpg хорошего качества)
<a name="top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p>
    <img src="https://github.com/fangorntreabeard/cval-lib/blob/main/images/on_premise.png?raw=true" width="70%" height="70%" alt="scheme">
  </p>
</div>

Fig 1. Working with the service according to the On-Premise scheme

In this version, the client library supports only the On-Premise scheme and allows working with the detection task. Interaction with the service according to the scheme All in Service is carried out through the Rest API, supported solutions of classification and detection tasks.
