# Copyright (c) 2024, krishna@aerele.in and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class TyreJobCard(Document):
	pass

@frappe.whitelist()
def fetch_details(doc):
	doc = json.loads(doc)
	if doc.get('vehicle_no'):
		vehicle_no = doc.get('vehicle_no')
		print('vehicle_no: ', vehicle_no)
		vehicle_detail = frappe.get_doc('Vehicle', {'name': vehicle_no})
		if len(vehicle_detail.custom_current_owner):
			customer = frappe.get_doc('Customer', {'name': vehicle_detail.custom_current_owner[0].current_owner, 'disabled': 0})
			doc['customer'] = customer.get('customer_name')
		if len(vehicle_detail.custom_current_driver):
			driver = frappe.get_doc('Driver', {'name': vehicle_detail.custom_current_driver[0].driver, 'status': "Active"})
			doc['driver1'] = driver.get('full_name')
		# if customer_detail.custom_current_driver:
		# 	driver = frappe.get_doc('Driver', {'name': customer_detail.custom_current_driver[0].full_name})
		# 	doc['driver1'] = driver.get('full_name')
		
	return doc