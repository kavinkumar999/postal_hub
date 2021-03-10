# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from postal_hub.postal_hub.doctype import facebook , twitter, insta 

__version__ = '0.0.1'

def posting(doc,caption):
	insta(caption)
	facebook(caption)
	twitter(caption)