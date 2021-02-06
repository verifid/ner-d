ner-d
=====

.. image:: https://img.shields.io/pypi/v/ner-d.svg
    :target: https://pypi.org/pypi/ner-d/

.. image:: https://img.shields.io/pypi/pyversions/ner-d.svg
    :target: https://pypi.org/project/ner-d

.. image:: https://travis-ci.org/verifid/ner-d.svg?branch=master
    :target: https://travis-ci.org/verifid/ner-d

.. image:: https://codecov.io/gh/verifid/ner-d/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/verifid/ner-d

.. image:: https://pepy.tech/badge/ner-d
    :target: https://pepy.tech/project/ner-d

**ner-d** is a Python module for Named Entity Recognition (NER). Named entity recognition (NER) (also known as entity identification, entity chunking and entity extraction)
is a subtask of information extraction that seeks to locate and classify named entity mentions in unstructured text into pre-defined categories such as the person
names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.

Gives you easy use with a single main function and flexibility for selecting language models. It automatically downloads models if not downloaded before and links on system
and finds the entities from given text block.

Prerequisites
=============

* A single dependency listed on ``requirements.txt`` and will be installed when you install with **pip**.

Installation
============

* Install module using ``pip``::

    $ pip install ner-d


* Download the latest ``ner-d`` library from: https://github.com/verifid/ner-d and install module using ``pip``::

    $ pip install -e .

* Extract the source distribution and run::

    $ python setup.py build
    $ python setup.py install

Usage
=====

* ``ner``:

.. code:: python

    from nerd import ner

    doc = ner.name("""GitHub launched April 10, 2008, a subsidiary of Microsoft, is an American web-based hosting service for version control using Git.
                       It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality
                       of Git as well as adding its own features.""", language='en_core_web_sm')
    text_label = [(X.text, X.label_) for X in doc]
    print(text_label)
    // [(u'GitHub', u'ORG'), (u'April 10, 2008', u'DATE'), (u'Microsoft', u'ORG'), (u'American', u'NORP'), (u'Git', u'PERSON'), (u'SCM', u'ORG'), (u'Git', u'PERSON')]

CLI
===

.. code:: bash

    // Downloads language model
    python -m nerd -d en_core_web_sm

    // Load language model
    python -m nerd -l en_core_web_sm

    // Find entities from text
    python -m nerd -n "GitHub launched April 10, 2008, a subsidiary of Microsoft, is an American web-based hosting service for version control using Git.
                       It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality
                       of Git as well as adding its own features."
