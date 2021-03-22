# -*- coding: utf-8 -*-
# Copyright (c) 2021, kavin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from instabot import Bot
from postal_hub import posting
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
	file_doc = frappe.get_doc("File", {"file_url":f'/private/files/{image}'})
	get_doc.post_image = file_doc.file_url
	# print(file_doc.file_url)
	# posting(doc,get_doc.caption)
	get_doc.save()

@frappe.whitelist() # Created the field and return to the primary key	
def created_doc(caption, facebook, insta, tweet):
	new_doc = frappe.new_doc("Postal Post")
	new_doc.caption = caption
	new_doc.facebook = 1 if facebook else 0
	new_doc.instagram = 1 if facebook else 0
	new_doc.twitter =  1 if facebook else 0
	new_doc.save()
	return str(new_doc.name)


@frappe.whitelist()
def image(docname):
	mode = frappe.get_doc("Postal Post","d4a93411b6")
	print(mode.post_image)
	return mode.post_image

	
	

