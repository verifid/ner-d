# Installation & Testing

## Installation

**From PyPI**

    $ pip install ner-d

**From source**

Install dependencies using `pip`

```console
$ pip install -r requirements.txt
```

Download the latest `ner-d` library from: https://github.com/verifid/ner-d

Extract the source distribution and run

```console
$ python setup.py build
$ python setup.py install
```

## Running Tests

The test suite can be run against a single Python version which requires `pip install pytest` and optionally `pip install pytest-cov` (these are included if you have installed dependencies from `requirements.testing.txt`)

To run the unit tests with a single Python version

```console
$ py.test -v
```

to also run code coverage

```console
$ py.test -v --cov-report html --cov=ner-d
```

## Getting the code

The code is hosted at [Github](https://github.com/verifid/ner-d).

Check out the latest development version anonymously with

```console
$ git clone https://github.com/verifid/ner-d.git
$ cd ner-d
```
