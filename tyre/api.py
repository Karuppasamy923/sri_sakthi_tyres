import frappe
import datetime
import json
import re

# function to get the vehicle & customer details (parameter = license plate)
@frappe.whitelist(allow_guest=True)
def get_details(license_plate):
	license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
	regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
	p = re.compile(regex)
	# regex = "^[A-Z]{2}[\\s-]{0,1}[0-9]{2}[\\s-]{0,1}[A-Z]{1,2}[\\s-]{0,1}[0-9]{4}$"
	# p = re.compile(regex)
	license_plate=license_plate.upper()
	if license_plate is None:
		print("error")
		return "NO Data Found!!!!"
	else:   
		print(license_plate)
		if(re.search(p, license_plate)):
			print("currect")
			print(license_plate)
			if license_plate:
				vehicle_details = ''
				customer_details = ''
				primary_details=[]

				# Check if Vehicle Details exist
				if frappe.db.exists("Vehicle Details", {"name": license_plate}):
					vehicle_details = frappe.get_doc("Vehicle Details", {"name": license_plate})

				# Check if Customer Details exist
				if frappe.db.exists("Customer Details", {"name": license_plate}):
					customer_details = frappe.get_doc("Customer Details", {"name": license_plate})
					for current_driver in customer_details.current_driver:
						data= frappe.get_doc("Driver",{"name":current_driver.current_driver})
						print(data.full_name)
						current_driver.name=current_driver.current_driver
						current_driver.current_driver=data.full_name
						if data.custom_primary:
							primary_details.append(data)
			   
				
					for contact_person in customer_details.contact_person:
						data= frappe.get_doc("ContactPerson",{"name":contact_person.contact_person_name})
						# print(data.contact_person_name)
						contact_person.name=contact_person.contact_person_name
						contact_person.contact_person_name=data.contact_person_name
						# print(contact_person.contact_person_name)
						if data.custom_primary:
							primary_details.append(data)
							
					# print(customer_details.current_owner)
				

				# print(customer_details.call)
				print("Vehicle Details:", vehicle_details)
				print("Customer Details:", customer_details)
				# print(customer_details.employee_name)

				if vehicle_details or customer_details :
					return [vehicle_details, customer_details,primary_details]
				else:
					return ""
		else:
			return "Enter a Valid vehicle number"        


# function to store new vehicle details
@frappe.whitelist(allow_guest=True)
def store_vehicle_details(data):
	data = json.loads(data)
	license_plate = data.get('name').upper().replace(' ', '')
	license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
	regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
	p = re.compile(regex)
	license_plate=license_plate.upper()
	print(license_plate)
	
	# checking if vehicle number already exists
	if(re.search(p, license_plate)):
		if frappe.db.exists('Vehicle Details', {'name': license_plate}):
			doc = frappe.get_doc('Vehicle Details', license_plate)
			doc.license_plate = license_plate
			doc.vehicle_brand = " ".join([w.capitalize() for w in data.get('vehicle_brand').split()]) if data.get('vehicle_brand') else None
			doc.vehicle_model = " ".join([w.capitalize() for w in data.get('vehicle_model').split()]) if data.get('vehicle_model') else None
			doc.chassis_no = data.get('chassis_no').upper() if data.get('chassis_no') else None
			doc.fuel_type = data.get('fuel_type')
			doc.last_odometer_reading = data.get('last_odometer_reading')
			doc.alignment = data.get('alignment')
			doc.tyre_change=data.get('tyre_change')
			doc.save(ignore_permissions=True)
			return [doc]
		else:
			doc = frappe.new_doc('Vehicle Details')
			doc.license_plate = license_plate
			doc.vehicle_brand = " ".join([w.capitalize() for w in data.get('vehicle_brand').split()]) if data.get('vehicle_brand') else None
			doc.vehicle_model = " ".join([w.capitalize() for w in data.get('vehicle_model').split()]) if data.get('vehicle_model') else None
			doc.chassis_no = data.get('chassis_no').upper() if data.get('chassis_no') else None
			doc.fuel_type = data.get('fuel_type')
			doc.last_odometer_reading = data.get('last_odometer_reading')
			doc.alignment = data.get('alignment')
			doc.tyre_change=data.get('tyre_change')
			doc.save(ignore_permissions=True)
			return [doc]
	else:
		return "Enter a valid number"    
	# # not in FE
	#     # doc.wheel

	# doc.save(ignore_permissions=True)

# function to store new customer details
@frappe.whitelist(allow_guest=True)
def store_customer_details(data):
	data = json.loads(data)
	print(data)
	license_plate = data.get('name').upper().replace(' ', '')
	license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
	regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
	p = re.compile(regex)
	print(license_plate)

	if(re.search(p, license_plate)):
		if frappe.db.exists('Customer Details', {'name': license_plate}):
			doc=frappe.get_doc('Customer Details', {'name': license_plate})
			doc.license_plate = license_plate
			if frappe.db.exists("Customer",{'name':data.get('owner_data')}):
				owner = frappe.get_doc("Customer",data.get('owner_data'))
				owner.customer_name = data.get( 'current_owner')
				owner.mobile_no = data.get('owner_mobile_no')
				owner.custom_whatsapp = data.get('whatsapp')
				owner.custom_sms = data.get('sms')
				owner.custom_call = data.get('call')
				owner.save(ignore_permissions=True)
			# doc.owner_email_id = data.get('owner_email_id')
			print("********old*******")
		
			#update a driver and conteact person
			for driver_data in data.get('employees', []):
				doc_type = driver_data.get('type')
				if doc_type == "current_driver":
					driver = frappe.db.get_value("Driver",{"name":driver_data.get('name')})
					print(driver_data.get('name'))
					# Append the name of the current_driver to the parent document
					if not driver:
						new_driver = frappe.new_doc("Driver")
						new_driver.full_name=driver_data.get('current_driver')
						new_driver.cell_number=driver_data.get('mobile_no')
						new_driver.custom_whatsapp_check=driver_data.get('whatsapp')
						new_driver.custom_sms_check=driver_data.get('sms')
						new_driver.custom_call_check=driver_data.get('call')
						new_driver.custom_primary=driver_data.get('primary')
						new_driver.save(ignore_permissions=True)
						driver = new_driver.name
						doc.append("current_driver", {"current_driver": driver, "mobile_no": driver_data.get('mobile_no')})
					else:
						print("11111111111")
						new_driver=frappe.get_doc("Driver",{"name":driver_data.get('name')})
						print(driver_data.get('current_driver'))
						new_driver.full_name=driver_data.get('current_driver')
						print("2222")
						new_driver.cell_number=driver_data.get('mobile_no')
						print("333")
						new_driver.custom_whatsapp_check=driver_data.get('whatsapp')
						new_driver.custom_sms_check=driver_data.get('sms')
						new_driver.custom_call_check=driver_data.get('call')
						if driver_data.get('primary')== True:
							new_driver.custom_primary=1
						else:
							new_driver.custom_primary=0    
						new_driver.save(ignore_permissions=True)
						# driver = new_driver.name  
				else:
					cPerson = frappe.db.get_value("ContactPerson",{"name":driver_data.get('name')})
					print(cPerson)
					if not cPerson:
						print("#######")
						new_driver = frappe.new_doc("ContactPerson")
						new_driver.contact_person_name=driver_data.get('contact_person_name')
						print(new_driver.contact_person_name)
						new_driver.contact_person_mobile=driver_data.get('contact_person_mobile')
						print(new_driver.contact_person_mobile)
						new_driver.whatsapp=driver_data.get("custom_whatsapp")
						new_driver.sms=driver_data.get("custom_sms")
						new_driver.call=driver_data.get("custom_call")
						new_driver.custom_primary=driver_data.get('custom_primary')
						new_driver.save(ignore_permissions=True)
						cPerson = new_driver.name
						doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile": driver_data.get('contact_person_mobile')})
					else:
						print("@@@@@@")
						new_driver=frappe.get_doc("ContactPerson",{"name":driver_data.get('name')})
						new_driver.contact_person_name=driver_data.get('contact_person_name')
						print(new_driver.contact_person_name)
						new_driver.contact_person_mobile=driver_data.get('contact_person_mobile')
						print(new_driver.contact_person_mobile)
						new_driver.whatsapp=driver_data.get("custom_whatsapp")
						new_driver.sms=driver_data.get("custom_sms")
						new_driver.call=driver_data.get("custom_call")
						# new_driver.custom_primary=driver_data.get('primary')
						if driver_data.get('custom_primary')== True:
							new_driver.custom_primary=1
						else:
							new_driver.custom_primary=0
						new_driver.save(ignore_permissions=True)
						# cPerson = new_driver.name 
					# Append new Contact Person document to the parent document
					#doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})

			# doc.save(ignore_permissions=True)  # Save customer document
			doc.save(ignore_permissions=True)
			frappe.db.commit()
			return ['',[doc]]
		##customer details doc not created then run this else 
		else:
			print("******new******")
			# New document in customer details
			doc = frappe.new_doc('Customer Details')
			doc.license_plate = license_plate
			owner = frappe.db.get_value("Customer",{"customer_name":data.get('current_owner'),"mobile_no":data.get('owner_mobile_no')})
			if not owner:
				new_owner=frappe.new_doc("Customer")
				new_owner.customer_name = data.get('current_owner')
				new_owner.mobile_no = data.get('owner_mobile_no')
				new_owner.custom_whatsapp=data.get('whatsappChecked')
				new_owner.custom_sms=data.get('smsChecked')
				new_owner.custom_call=data.get('callChecked')
				new_owner.save(ignore_permissions=True)
				doc.owner_data=new_owner
			# doc.owner_email_id = data.get('owner_email_id')
			else:
				frappe.throw("already owner of exsist with given number"+data.get('owner_mobile_no'))

			# New driver or contact person document
			for driver_data in data.get('employees', []):
				doc_type = driver_data.get('type')
				if doc_type == "current_driver":
					driver = frappe.db.get_value("Driver",{"cell_number":driver_data.get('mobile_no')})
					# Append the name of the current_driver to the parent document
					if not driver:
						new_driver = frappe.new_doc("Driver")
						new_driver.full_name=driver_data.get('driver_name')
						new_driver.cell_number=driver_data.get('mobile_no')
						new_driver.custom_whatsapp_check=driver_data.get('whatsappChecked1')
						new_driver.custom_sms_check=driver_data.get('smsChecked1')
						new_driver.custom_call_check=driver_data.get('callChecked1')
						new_driver.custom_primary=driver_data.get('primary')
						new_driver.save(ignore_permissions=True)
						driver = new_driver.name
					doc.append("current_driver", {"current_driver": driver, "mobile_no": driver_data.get('mobile_no')})
				else:
					cPerson = frappe.db.get_value("ContactPerson",{"contact_person_mobile":driver_data.get('mobile_no')})
					if not cPerson:
						new_driver = frappe.new_doc("ContactPerson")
						print(driver_data.get('driver_name'))
						new_driver.contact_person_name=driver_data.get('driver_name')
						new_driver.contact_person_mobile=driver_data.get('mobile_no')
						new_driver.whatsapp=driver_data.get('whatsappChecked1')
						new_driver.sms=driver_data.get('smsChecked1')
						new_driver.call=driver_data.get('callChecked1')
						print("primary",driver_data.get('primary'))
						new_driver.custom_primary=driver_data.get('primary')
						print(new_driver.custom_primary)
						new_driver.save(ignore_permissions=True)
						cPerson = new_driver.name
					# Append new Contact Person document to the parent document
					doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})

			# doc.save(ignore_permissions=True)  # Save customer document
			doc.save(ignore_permissions=True)
			frappe.db.commit()
			return ['',[doc]]
	else:
		return "Enter a valid number"


# function to create job card
@frappe.whitelist(allow_guest=True)
def job_card(data):
	five_point_checkup = {}
	tyre_abbr = {"Rear Left": "rl_", "Front Right": "fr_", "Front Left": "fl_", "Rear Right": "rr_","Spare Tyre": "sp1_"}
	for checkup in data.checkup:
		abbr = tyre_abbr[checkup.tyre]
		five_point_checkup.update({
				abbr + "remaining_tread_depth": checkup.depth,
				abbr + "tyre_pressure": checkup.pressure,
				abbr + "comment": checkup.comment,
				abbr + "irregular_wear": checkup.wear,
				abbr + "run_flat_mark": checkup.mark,
				abbr + "bulge": checkup.bulge,
				abbr + "cut_damage": checkup.cut,
				abbr + "damage": checkup.damage,
				abbr + "inflation": checkup.puncture,
		})
	tyre_replacement = {}
	tyre_types = {"Front-Left": "fl", "Front-Right": "fr", "Back-Left": "rl", "Back-Right": "rr", "Stephanie": "sp"}
	for replacement in data.replace:
		abbr = tyre_types[replacement.tyre]
		tyre_replacement.update({
				abbr + "_brand": replacement.brand,
				abbr + "_load_index": replacement.loadIndex,
				abbr + "_pattern": replacement.pattern,
				abbr + "_speed_rating": replacement.speedRating,
				abbr + "_tt_tl": replacement.ttTl,
				abbr + "_size": replacement.size,
				abbr + "_item": replacement.item
		})
		
@frappe.whitelist(allow_guest=True)
def get_brand_details():
	result = {}
	data = frappe.db.sql(""" SELECT  Distinct b.name,bp.pattern,bp.size,s.load_index,s.speed_rating,bp.tyer_type  FROM `tabBrand` as b 
						join `tabBrand Details` as bp on b.name = bp.parent 
						 JOIN `tabSize` as s ON bp.size = s.name """,as_dict=True)

	# print(data)
	for row in data:

		if row.name not in result:
			result[row.name] = {row.size: [{"load_index": row.load_index,"speed_rating": row.speed_rating, "tyer_type": row.tyer_type , "pattern": row.pattern}]}

		elif row.size in result[row.name]:
			result[row.name][row.size].append({"load_index": row.load_index,"speed_rating": row.speed_rating, "tyer_type": row.tyer_type , "pattern": row.pattern})


		elif row.size not in result[row.name]:
			result[row.name][row.size] = [{"load_index": row.load_index,"speed_rating": row.speed_rating, "tyer_type": row.tyer_type , "pattern": row.pattern}]

	return result

# function to create job card
@frappe.whitelist(allow_guest=True)
def stock_details():
	items_grouped_by_brand = []
	items = frappe.get_all("Item", filters={"has_variants": 1}, fields=["name", "item_name", "brand"])

	for item in items:
		item_data = {
			"name": item['item_name'],
			"variants": []
		}
		variants = frappe.get_all("Item", filters={"variant_of": item['name']}, fields=["name", "item_name"])
		
		for variant in variants:
			item_data["variants"].append(variant['item_name'])
		
		items_grouped_by_brand.append(item_data)

	print(items_grouped_by_brand)
	return items_grouped_by_brand
