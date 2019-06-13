#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('all')

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
