# -*- coding: utf-8 -*-
# Copyright (c) 2021, kavin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PostalPost(Document):
	pass

@frappe.whitelist()
def get_data():
	result = frappe.db.sql("""select post_image,caption from `tabPostal Post`""",as_dict = 1)
	return result

@frappe.whitelist()
def insert_data():
	print("image,caption")

	# new_doc = frappe.new_doc("Postal Post")
	# new_doc.post_image = image
	# new_doc.caption = caption
	# new_doc.save()


