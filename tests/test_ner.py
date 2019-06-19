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

    def test_name(self):
        doc = ner.name('GitHub launched April 10, 2008, a subsidiary of Microsoft, is an American web-based hosting service for version control using Git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.')
        self.assertEqual(doc, 'GitHub launched April 10, 2008, a subsidiary of Microsoft, is an American web-based hosting service for version control using Git. It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.')
        print(doc.ents)
