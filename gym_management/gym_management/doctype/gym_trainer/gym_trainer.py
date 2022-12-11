# Copyright (c) 2022, Lance and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class GymTrainer(Document):
	def before_insert(self):
		self.full_name = self.first_name + " " + self.last_name
