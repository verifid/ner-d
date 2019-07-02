#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from nerd import ner

class NerTest(unittest.TestCase):

    def test_load_model(self):
        nlp = ner.load_model()
        self.assertIsNotNone(nlp)

    def test_name(self):
        doc = ner.name("""GitHub launched April 10, 2008, a subsidiary of Microsoft, is an American web-based hosting service for version control using Git.
                       It is mostly used for computer code. It offers all of the distributed version control and source code management (SCM) functionality
                       of Git as well as adding its own features.""", language='en_core_web_sm')
        text_label = [(X.text, X.label_) for X in doc]
        self.assertEqual(text_label, [(u'GitHub', u'ORG'), (u'April 10, 2008', u'DATE'), (u'Microsoft', u'ORG'), (u'American', u'NORP'), (u'Git', u'PERSON'), (u'SCM', u'ORG'), (u'Git', u'PERSON')])
        doc = ner.name("""Michael Jeffrey Jordan born February 17, 1963 in Brooklyn, New York, United States of America. Known by his initials, MJ,[5] is an American former professional
                       basketball player who is the principal owner and chairman of the Charlotte Hornets of the National Basketball Association
                       """, language='en_core_web_sm')
        text_label = [(X.text, X.label_) for X in doc]
        self.assertEqual(text_label, [('Michael Jeffrey Jordan', 'PERSON'), ('February 17, 1963', 'DATE'), ('Brooklyn', 'GPE'), ('New York', 'GPE'), ('United States of America', 'GPE'), ('MJ,[5', 'ORG'), ('American', 'NORP'), ('the Charlotte Hornets', 'LOC'), ('the National Basketball Association', 'ORG')])
