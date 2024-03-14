# Copyright (c) 2024, krishna@aerele.in and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class VehicleDetails(Document):
	def validate(self):
		self.license_plate = self.license_plate.upper().replace(' ', '')

