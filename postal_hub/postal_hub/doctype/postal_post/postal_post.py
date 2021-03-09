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
	return "success"

@frappe.whitelist()  # Add the image from the attachment to the field
def data_to_field(doc,image):
	get_doc = frappe.get_doc("Postal Post",doc)
	file_doc = frappe.get_doc("File", {"file_url":f'/private/files/{image}.jpg'})
	new_doc.post_image = file_doc.file_url
	get_doc.save()

@frappe.whitelist() # Created the field and return to the primary key	
def created_doc(caption):
	new_doc = frappe.new_doc("Postal Post")
	new_doc.caption = caption
	new_doc.save()
	return new_doc.name

@frappe.whitelist()
def posting(doc):
	print("post")
	
	

