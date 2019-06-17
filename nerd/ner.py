#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import spacy

from spacy.cli.download import download
from spacy.cli import link
from spacy.util import get_package_path

supported_languages = ['en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
                       'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
                       'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm']

def download_model(model_name):
    download(modelname)
    package_path = get_package_path(model_name)
link(model_name, model_name, force=True, package_path=package_path)

def load_model(language='en_core_web_sm'):
    """
    Loads language trained model.

        >>> from nerd import ner
        >>> ner.load_model(language='en_core_web_sm')
        >>> or
        >>> ner.load_model(language='de_core_news_sm')
        >>> supported languages 'en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
        'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
        'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm'

    :param language: Language package name, shortcut link or model path.
    :type language: str
    :rtype: `Language` class with the loaded model.
    """

    if language not in supported_languages:
        return None
    download_model(language)
    nlp = spacy.load(language)
    return nlp
