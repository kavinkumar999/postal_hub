// Copyright (c) 2016, kavin and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Post Analytics"] = {
	"filters": [
		{
			"fieldname": "user",
			"fieldtype": "Link",
			"label": "User",
			"options": "User",
		},
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": "From Date",
		},
		{
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": "To Date",
		}

	]
};
