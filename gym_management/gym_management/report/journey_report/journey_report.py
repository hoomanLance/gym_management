# Copyright (c) 2022, Lance and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = get_data(filters)

	return columns, data

def get_columns():
	return [
		{
			"label": "Full Name",
			"fieldname": "full_name",
			"fieldtype": "Link",
			"options": "Gym Member",
		},
		{
			"label": "Membership Type",
			"fieldname": "membership_type",
			"fieldtype": "Link",
			"options": "Gym Member"
		},
		{
			"label": "Date",
			"fieldname": "date",
			"fieldtype": "Link",
			"options": "metrics"
		},
		{
			"label": "Weight",
			"fieldname": "weight",
			"fieldtype": "Link",
			"options": "metrics"
		},
		{
			"label": "Calories Intake",
			"fieldname": "calories_intake",
			"fieldtype": "Link",
			"options": "metrics"
		},
		{
			"label": "Workout Duration",
			"fieldname": "workout_duration",
			"fieldtype": "Link",
			"options": "metrics"
		}
	]
def get_data(filters):
	metrics_details = frappe.get_all("Gym Member",
		fields = ["full_name", "membership_type"],
	)
	metrics_cond = ""

	if filters.get("full_name"):
		metrics_cond = f" AND `tabGym Member`.full_name = '{filters.full_name}'"
	
	gym_member_details = frappe.db.sql(f"""
		SELECT
			`tabGym Member`.full_name as full_name,
			`tabGym Member`.membership_type,
			`tabGym Member Metrics`.date,
			`tabGym Member Metrics`.weight,
			`tabGym Member Metrics`.calories_intake,
			`tabGym Member Metrics`.workout_duration
		FROM
			`tabGym Member`, `tabGym Member Metrics`
		WHERE
			`tabGym Member`.name = `tabGym Member Metrics`.parent
			{metrics_cond}
	""", as_dict=1)

	journey_details = {}
	for row in gym_member_details:
		journey_details.setdefault(row.full_name, []).append(row)
	
	data = []
	# frappe.errprint(journey_details)
	# frappe.errprint(gym_member_details)
	for metrics in metrics_details:
		metrics_dict = {
			"full_name": metrics.full_name,
			"membership_type": metrics.membership_type,
		}	
		if journey_details.get(metrics.full_name):
			for journey in journey_details.get(metrics.full_name):
				metrics_dict.update({
					"date": journey.date,
					"weight": journey.weight,
					"calories_intake": journey.calories_intake,
					"workout_duration": journey.workout_duration,
				})
				data.append(metrics_dict)

	return data