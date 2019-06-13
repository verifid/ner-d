#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import spacy

__download_url__ = "https://github.com/explosion/spacy-models/releases/download"
__version__ = '2.1.0'
supported_languages = ['en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
                       'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
                       'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm']

def download_model(filename):
    cmd = [sys.executable, '-m', 'spacy', 'download', filename]
    return subprocess.call(cmd, env=os.environ.copy())

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
