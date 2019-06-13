#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('all')

__download_url__ = "https://github.com/explosion/spacy-models/releases/download"
supported_languages = ['en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
                       'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
                       'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm']

def download_model(filename, user_pip_args=None):
    download_url = __download_url__ + "/" + filename
    pip_args = ["--no-cache-dir", "--no-deps"]
    if user_pip_args:
        pip_args.extend(user_pip_args)
    cmd = [sys.executable, "-m", "pip", "install"] + pip_args + [download_url]
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

def preprocess(text, lang_tokenize='english', lang_tag='eng'):
    """
    Preprocesses given text with optional language parameter.

        >>> from nerd import ner
        >>> ner.preprocess('The four-time Tour de France champion, 34,
        has suffered a fractured right femur, a broken hip, a fractured
        elbow and fractured ribs and lost consciousness following the crash.')

    :param text: Sequence text.
    :type text: str
    :param lang_tokenize: the model name in the Punkt corpus
    :type lang_tokenize: str
    :param lang: the ISO 639 code of the language, e.g. 'eng' for English, 'rus' for Russian
    :type lang: str
    :return: The tagged tokens
    :rtype: list(tuple(str, str))
    """

    text = nltk.word_tokenize(text)
    text = nltk.pos_tag(text)
    return text
