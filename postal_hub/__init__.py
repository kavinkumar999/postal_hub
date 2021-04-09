# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from postal_hub.postal_hub.doctype import facebook , twitter, insta 
import frappe
from postal_hub.postal_hub.doctype.postal_post.postal_post import post
__version__ = '0.0.1'

@frappe.whitelist()
def scheduledpost():
	# query
	posted = frappe.db.get("select post_image, caption, is_complete ,post_time ,name from `tabPostal Post` where is_complete = 0",as_dict = 1)
	for _post in posted:
		if _post["post_time"] < frappe.utils.now():
			post(_post["name"])
	print("scheduledpost")

@frappe.whitelist()
def posting():
	return "posted"
