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
