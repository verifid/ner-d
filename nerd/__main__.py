#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from nerd import ner

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='CLI - Python module for Named Entity Recognition (NER).')
    parser.add_argument('-d', '--download', type=str, help='Language model name to download.')
    parser.add_argument('-l', '--load', type=str, help='Load downloaded language model.')
    parser.add_argument('-n', '--name', type=str, help='Find entities from given text.')
    args = parser.parse_args()

    if len(sys.argv) < 2:
        print('Specify a key to use')
        sys.exit(1)

    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    args = parser.parse_args()
    if args.download != None:
        ner.download_model(args.download)
    elif args.load != None:
        ner.load_model(args.load)
    else:
        doc = ner.name(args.name)
        text_label = [(X.text, X.label_) for X in doc]
        print(text_label)
