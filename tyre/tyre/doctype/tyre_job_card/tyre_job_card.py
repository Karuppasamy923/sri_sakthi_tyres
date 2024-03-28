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
		vehicle_detail = frappe.get_doc('Vehicle Details', {'name': vehicle_no})
		if len(vehicle_detail.current_owner):
			customer = frappe.get_doc('Current Owner', {'name': vehicle_detail.current_owner})
			doc['current_owner'] = customer.get('current_owner')
			
		# if len(vehicle_detail.custom_current_driver):
			# driver = frappe.get_doc('Driver', {'name': vehicle_detail.custom_current_driver[0].driver, 'status': "Active"})
			# doc['driver1'] = driver.get('full_name')
		# if customer_detail.custom_current_driver:
		# 	driver = frappe.get_doc('Driver', {'name': customer_detail.custom_current_driver[0].full_name})
		# 	doc['driver1'] = driver.get('full_name')
		print('doc', doc)
	return doc