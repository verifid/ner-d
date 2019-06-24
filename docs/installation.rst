Installation & Testing
----------------------

Installation
============

**From PyPI** ::

    $ pip install ner-d

**From source**

Install module using `pip`::

    $ pip install -e .

Download the latest `ner-d` library from: https://github.com/verifid/ner-d

Extract the source distribution and run::

    $ python setup.py build
    $ python setup.py install

Running Tests
=============

The test suite can be run against a single Python version which requires ``pip install pytest`` and optionally ``pip install pytest-cov`` (these are included if you have installed dependencies from ``requirements.testing.txt``)

To run the unit tests with a single Python version::

    $ py.test -v

to also run code coverage::

    $ py.test -v --cov-report html --cov=ner-d

Getting the code
================

The code is hosted at `Github <https://github.com/verifid/ner-d>`_.

Check out the latest development version anonymously with::

$ git clone https://github.com/verifid/ner-d.git
$ cd ner-d
