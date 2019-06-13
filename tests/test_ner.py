#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pytest
import os

from nerd import ner

class NerTest(unittest.TestCase):

    def test_preprocess(self):
        result = ner.preprocess('The four-time Tour de France champion, 34,'
        + 'has suffered a fractured right femur, a broken hip, a fractured'
        + 'elbow and fractured ribs and lost consciousness following the crash.')
        self.assertEqual(result, [('The', 'DT'), ('four-time', 'JJ'), ('Tour', 'NNP'), ('de', 'FW'), ('France', 'NNP'), ('champion', 'NN'), (',', ','), ('34', 'CD'), (',', ','), ('has', 'VBZ'), ('suffered', 'VBN'), ('a', 'DT'), ('fractured', 'JJ'), ('right', 'NN'), ('femur', 'NN'), (',', ','), ('a', 'DT'), ('broken', 'JJ'), ('hip', 'NN'), (',', ','), ('a', 'DT'), ('fracturedelbow', 'NN'), ('and', 'CC'), ('fractured', 'VBD'), ('ribs', 'NNS'), ('and', 'CC'), ('lost', 'VBN'), ('consciousness', 'NN'), ('following', 'VBG'), ('the', 'DT'), ('crash', 'NN'), ('.', '.')])
        result = ner.preprocess('Michael Jordan born 17.02.1963 in New York is an American basketballer.')
        self.assertEqual(result, [('Michael', 'NNP'), ('Jordan', 'NNP'), ('born', 'VBD'), ('17.02.1963', 'CD'), ('in', 'IN'), ('New', 'NNP'), ('York', 'NNP'), ('is', 'VBZ'), ('an', 'DT'), ('American', 'JJ'), ('basketballer', 'NN'), ('.', '.')])
