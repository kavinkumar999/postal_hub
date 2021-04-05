# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from postal_hub.postal_hub.doctype import facebook , twitter, insta 
import frappe
__version__ = '0.0.1'

@frappe.whitelist()
def scheduledpost():
	print("scheduledpost")

@frappe.whitelist()
def posting():
	print("posting")
