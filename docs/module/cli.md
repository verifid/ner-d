# CLI

CLI helps you to download and load language models as well as naming entities from texts.

## Usage

First you need to install **ner-d** either from PyPi or source. Then you can use sample
commands below.

Download language model of spacy

```console
$ python -m nerd -d en_core_web_sm
```

Load language model after downloading

```console
$ python -m nerd -l en_core_web_sm
```

Recognize name entities from text

```console
$ python -m nerd -n "Michael Jeffrey Jordan born February 17, 1963 in Brooklyn, New York, United States of America."
```
