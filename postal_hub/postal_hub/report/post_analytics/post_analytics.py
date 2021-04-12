# Copyright (c) 2013, kavin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []
	if "from_date" in filters and "to_date" in filters:
		data = get_data(filters)
	columns = get_columns()
	return columns, data

def get_columns():
	columns = [
		{
			"fieldname":"postcode",
			"label": "Post Id",
			"fieldtype": "Link",
			"options": "Postal Post"
		},
		{
			"fieldname":"caption",
			"label": "caption",
			"fieldtype": "Data",
		},
		{
			"fieldname":"postdate",
			"label": "Post Date",
			"fieldtype": "Date",
		},
		{
			"fieldname":"posted_by",
			"label": "Posted By",
			"fieldtype": "Data",
		},
		{
			"fieldname":"iscomplete",
			"label": "Is Complete",
			"fieldtype": "Check",
		},
		{
			"fieldname":"facebook",
			"label": "Facebook",
			"fieldtype": "Check",
		},
		{
			"fieldname":"twitter",
			"label": "Twitter",
			"fieldtype": "Check",
		},
		{
			"fieldname":"instagram",
			"label": "Instagram",
			"fieldtype": "Check",
		},
		
	]
	return columns

def get_data(filters):
	condition = ""
	if "user" in filters:
		condition = "and pp.owner = "+ "\'" + "{user}".format(user = str(filters.user)) + "\'"
	a =  frappe.db.sql("""select pp.name,pp.caption, pp.post_time  ,pp.owner, pp.is_complete,pd.facebook,pd.twitter,pd.instagram from `tabPostal Post` as pp inner join `tabPost Details` as pd on pp.detail = pd.name where pp.post_time > {from_} and pp.post_time <= {to_} {condition} order by  pp.post_time desc""".format(from_ = "\'" + str(filters.from_date) + "\'" , to_ = "\'" + str(filters.to_date) + "\'",condition =  condition),as_list=1)
	return a