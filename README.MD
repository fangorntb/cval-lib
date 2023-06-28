<!-- TOP OF README ANCHOR -->
<a name="top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <p>
    <img src="https://github.com/fangorntreabeard/cval-lib/blob/main/logo/logo.jpg?raw=true" alt="Cval logo" width="155" height="155">
  </p>

<h3 align="center">CVAL REST API LIBRARY</h3>

  <p align="center">
    A library designed to interact with the REST-API cval.ai
    <br/>
    <b>
      <a href="https://cval.ai">REST API docs</a>
      ·
      <a href="https://github.com/fangorntreabeard/cval-lib/issues">Report Bug</a>
    </b>
  </p>
</div>

# About

With CVAL, you can iteratively **improve your models** by following our active learning loop.

* **First**, manually or semi-automatically annotate a random set of images.

* **Next**, train your model and use uncertainty and diversity methods to score the remaining images for annotation.

* **Then**, manually or semi-automatically annotate the images marked as more confident to increase the accuracy of the model.

Repeat this process until you achieve an acceptable quality of the model.

# Getting started

To start using the CVAL Rest API, you need to **obtain** a **client/user API key**. 
Once you have your API key, you can use it to authenticate your requests and interact with the CVAL Rest API endpoints. 
Refer to our API documentation for detailed information on available endpoints, request formats, and response structures.

## Installation

#### Unix and Mac
```shell
python3 -m pip install cval-lib
```
or downloaded:

```shell
python3 -m pip install cval-lib.tar
```

#### Windows
```powershell
python -m pip install cval-lib
```
or downloaded:
```shell
python3 -m pip install cval-lib.tar
```

#### Submodule
```shell
git submodule add https://github.com/fangorntreabeard/cval-lib.git cval
```
## Architecture
The library architecture consists of **three layers**:
1. _A layer of protocols and abstract handlers_. Responsible for the use of a particular library. If an error is found, it is enough to simply change one method.
2. _A layer of handlers._ These are all the methods that are present in the API. Are based on abstract
3. _Model layer._ If the data structure changes, only this layer changes.

## Examples

##### Set your user_api_key

```python3
from cval_lib import CVALConnection
USER_API_KEY='awesome_api_key'
cval = CVALConnection(api_key)
```

> The same actions are available with the rest of the entities, but there are some nuances, for example, somewhere there is the use of models, and somewhere only parameters. But anyway, these examples well reflect possible scenarios when working with cval. 
> The most typical api scenario is a dataset, so let's start with it.

### Dataset
 > Within the framework of the created system, datasets are spaces in which data for machine learning is stored.
 Creating a dataset is similar to creating a folder.
##### Create dataset
```python3
# :NOTE: To avoid incomprehensibility of errors, it is recommended to use  CVALConnection
ds_id = cval.dataset().create(name='on-premise-scheme-ds', description='')
print(ds_id)
```

##### Update dataset
```python
ds = cval.dataset()
ds.update(ds_id, description='any string data')
# :NOTE: the dataset can store the state (ds_id)
ds.update(name='sample name')
```

##### Get dataset
```python
ds.get()
```

### Embeddings

##### Create embeddings

```python
from random import random
import uuid
from cval_lib.models.embedding import ImageEmbeddingModel

img_id_1 = str(uuid.uuid4())
img_id_2 = str(uuid.uuid4())

embeddings = [
 ImageEmbeddingModel(id=img_id_1, image_embedding=list(map(random, range(1000)))), 
 ImageEmbeddingModel(id=img_id_2, image_embedding=list(map(random, range(1000)))),
]
```

##### Upload embeddings
```python
emb = cval.embedding(ds_id)
emb.upload_many(embeddings)
print(emb.get_many())
```

##### Allow some access to global variables
```python
```

###### Output:
```text
bar
```

##### Allow access to all global variables
```python
foo = "bar"
bar = "foo"

def foobar():
    cval('print(bar+foo")', globals=globals(), allowed_global_vars=["*"], allowed_calls=["print"])
foobar()
```

###### Output:
```text
foobar
```

##### Block access local variables
```python
def fizzbuzz():
    fizz = "buzz"
    cval('print(fizz)', locals=locals())  # Will not be able to access "fizz"
fizzbuzz()
```

###### Output:
```text
cval.SuspiciousSource: Cval found local variable "fizz" in the source, killing for safety.
```

##### Allow some access to local variables
```python
def fizzbuzz():
    fizz = "buzz"
    cval('print(fizz)', locals=locals(), allowed_local_vars=["fizz"], allowed_calls=["print"])
fizzbuzz()
```

###### Output:
```text
buzz
```

##### Allow access to all local variables
```python
def fizzbuzz():
    fizz = "buzz"
    buzz = "fizz"
    cval('print(buzz+fizz)', locals=locals(), allowed_local_vars=["*"], allowed_calls=["print"])
fizzbuzz()
```

###### Output:
```text
fizzbuzz
```