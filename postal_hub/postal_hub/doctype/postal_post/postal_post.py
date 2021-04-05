# -*- coding: utf-8 -*-
# Copyright (c) 2021, kavin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from instabot import Bot
from postal_hub import posting
from frappe.model.document import Document
from datetime import timedelta
from datetime import datetime
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
def created_doc(caption, facebook, insta, tweet, future, hrs):
	new_doc = frappe.new_doc("Postal Post")
	new_doc.caption = caption
	detail =  frappe.new_doc("Post Details")
	detail.facebook = 1 if facebook == "1" else 0
	detail.instagram = 1 if insta == "1" else 0
	detail.twitter =  1 if tweet == "1" else 0
	detail.save()
	new_doc.detail = detail.name
	new_doc.is_complete = 1 if future == "0" else 0
	new_doc.post_time = datetime.strptime(frappe.utils.now(), '%Y-%m-%d %H:%M:%S.%f') + timedelta(hours = 0 if new_doc.is_complete == 1 else int(hrs))
	new_doc.save()
	return str(new_doc.name)


@frappe.whitelist()
def image(docname):
	mode = frappe.get_doc("Postal Post","d4a93411b6")
	print(mode.post_image)
	return mode.post_image


@frappe.whitelist()
def login():
	return "success"
	

@frappe.whitelist()
def data():
	result = frappe.db.sql("select * from `tabPostal Post` as post inner join `tabPost Details` as media on media.name=post.detail")
	return result


@frappe.whitelist()
def stackpost():
	stack = frappe.db.sql("select pp.post_image,pp.caption, pp.is_complete,pd.facebook,pd.instagram,pd.twitter,pp.post_time from `tabPostal Post` as pp inner join `tabPost Details` as pd on pp.detail = pd.name",as_list=1)
	for s in range(0,len(stack)):
		print(type(frappe.utils.now()))
		print(type(stack[s][6]))
		now = datetime.strptime(frappe.utils.now(), '%Y-%m-%d %H:%M:%S.%f')
		then = stack[s][6]
		print(type(now))
		print(type(then))
		balance = now - then
		bal_second = balance.total_seconds()
		stack[s][6] = divmod(bal_second,3600)[0]
	return stack


@frappe.whitelist()
def post(docname):
	return "success"
