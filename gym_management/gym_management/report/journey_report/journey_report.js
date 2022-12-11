// Copyright (c) 2022, Lance and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Journey Report"] = {
	"filters": [
		{
		fieldname: "full_name",
		label: __("Full Name"),
		fieldtype: "Link",
		options: "Gym Member",
		}
	]
};
