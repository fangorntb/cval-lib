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

To start using the CVAL Rest API, you need to obtain a client API key. 
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
py -m pip install cval-lib
```
or downloaded:
```shell
python3 -m pip install cval-lib.tar
```

#### Submodule
```shell
git submodule add https://github.com/fangorntreabeard/cval-lib.git cval
```
## Exploiting
I **encourage** you to break my script, report any bugs or vulnerabilities [here](https://github.com/ZackeryRSmith/cval/issues), thanks!

## Examples
These examples are focused purely on security rather then real world practical examples.

##### Disable module importing
```python
# :NOTE: modules is False by default, and the reason we allow function calls
#        is to see the error given when trying to import a module.
cval('__import__("os")', calls=True, modules=False)
```

###### Output:
```text
cval.IllegalSource: Cval panicked due to an attempted illegal import of the module "os"
```

##### Allow certain modules
```python
cval('__import__("os")', allowed_modules=["os"], allowed_calls=["import"])
```

##### Disable function calls
```python
cval('print("Hello, World!")', calls=False)
```

###### Output:
```text
cval.IllegalSource: Cval panicked due to an illegal function call in source! Attemped call to "print"
```

##### Allow certain function calls
```python
cval('print("Hello, World!")', allowed_calls=["print"])
```

##### Block access to global variables
```python
foo = "bar"

def foobar():
    # :NOTE: `globals` doesn't need to be passed in this case
    #        this is only done here for clarity 
    cval('print(foo)', globals=globals(), allowed_calls=["print"])  # Will not be able to access "foo"
foobar()
```

###### Output:
```text
cval.SuspiciousSource: Cval found global variable "foo" in the source, killing for safety.
```

##### Allow some access to global variables
```python
foo = "bar"

def foobar():
    cval('print(foo)', globals=globals(), allowed_global_vars=["foo"], allowed_calls=["print"])
foobar()
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