# Copyright (c) 2022, Lance and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymClassBooking(Document):
	def before_insert(self):
		self.full_name = frappe.session.user_fullname
		classData = frappe.get_doc("Gym Class", self.gym_class)
		self.class_trainer = classData.trainer_specialty
		scheduleLength = len(classData.schedule)
		
		for i in range(scheduleLength):
			row = self.append('schedule', {})
			row.class_date = classData.schedule[i].class_date
			row.class_start_time = classData.schedule[i].class_start_time
			row.class_end_time = classData.schedule[i].class_end_time
