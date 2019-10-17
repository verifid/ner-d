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
    """
    Downloads and links language trained model.

        >>> from nerd import ner
        >>> ner.download_model(model_name='en_core_web_sm')
        >>> supported languages 'en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
        >>> 'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
        >>> 'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm'

    :param model_name: Model package name.
    :type model_name: str
    """

    download(model_name)
    package_path = get_package_path(model_name)
    link(model_name, model_name, force=True, model_path=package_path)


def load_model(language='en_core_web_sm'):
    """
    Loads language trained model.

        >>> from nerd import ner
        >>> ner.load_model(language='en_core_web_sm')
        >>> or
        >>> ner.load_model(language='de_core_news_sm')
        >>> supported languages 'en_core_web_sm', 'de_core_news_sm', 'fr_core_news_sm',
        >>> 'es_core_news_sm', 'pt_core_news_sm', 'it_core_news_sm',
        >>> 'nl_core_news_sm', 'el_core_news_sm', 'xx_ent_wiki_sm'

    :param language: Language package name, shortcut link or model path.
    :type language: str
    :rtype: `Language` class with the loaded model.
    """

    if language not in supported_languages:
        return None
    download_model(language)
    nlp = spacy.load(language)
    return nlp


def name(text, language='en_core_web_sm'):
    """
    Find related name entities from given text.

        >>> from nerd import ner
        >>> ner.name('another text given as parameter for name entity recognition', language='en_core_web_sm')

    :param text: Group of words or sentences.
    :type text: str
    :param language: Language package name, shortcut link or model path.
    :type language: str
    :rtype: Entities found from given text.
    """

    try:
        nlp = spacy.load(language)
    except IOError:
        nlp = load_model(language)
    try:
        doc = nlp(unicode(text, 'utf-8'))
    except NameError:
        doc = nlp(text)
    return doc.ents
