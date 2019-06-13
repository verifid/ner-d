#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
import os

from nerd import ner

class NerTest(unittest.TestCase):

    def test_load_model(self):
        nlp = ner.load_model()
        self.assertIsNotNone(nlp)
        nlp = ner.load_model(language='de_core_news_sm')
        self.assertIsNotNone(nlp)
        nlp = ner.load_model(language='tr_core_news_sm')
        self.assertIsNone(nlp)
