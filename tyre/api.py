import frappe
import datetime
import json
import re

# function to get the vehicle & customer details (parameter = license plate)
@frappe.whitelist(allow_guest=True)
def get_details(license_plate):
	print("****")
	print(license_plate)
	license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
	regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
	p = re.compile(regex)
	# regex = "^[A-Z]{2}[\\s-]{0,1}[0-9]{2}[\\s-]{0,1}[A-Z]{1,2}[\\s-]{0,1}[0-9]{4}$"
	# p = re.compile(regex)
	license_plate=license_plate.upper()
	if license_plate is None:
		return "NO Data Found!!!!"
	else:   
		print(license_plate.upper())
		if(re.search(p, license_plate)):
			print("*****currect*******")
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
					print("*******")
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
	print(data)
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


@frappe.whitelist(allow_guest=True)
def lead_details(data):
	doc =  frappe.get_doc("Lead",{"mobile_no" : data})
	if not doc :
		return{
			"message": "Lead not found"
		}
	return doc

# function to create job card
@frappe.whitelist(allow_guest=True)
def job_card(data):
	print(data, type(data))
	data = frappe._dict(json.loads(data))
	# print(data.checkup)
	five_point_checkup = {}
	tyre_abbr = {"Rear Left": "rl_", "Front Right": "fr_", "Front Left": "fl_", "Rear Right": "rr_","Spare Tyre": "sp1_"}
	for checkup in data.checkup:
		checkup = frappe._dict(checkup)
		if checkup.tyre :
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
	tyre_types = {"Front Left": "fl", "Front Right": "fr", "Rear Left": "rl", "Rear Right": "rr", "Spare Tyre": "sp"}
	for replacement in data.replace:
		replacement = frappe._dict(replacement)
		if replacement.type :
			abbr = tyre_types[replacement.type]
			tyre_replacement.update({
					abbr + "_brand": replacement.brand,
					abbr + "_load_index": replacement.loadIndex,	
					abbr + "_pattern": replacement.pattern,
					abbr + "_speed_rating": replacement.speedRating,
					abbr + "_tt_tl": replacement.ttTl,
					abbr + "_size": replacement.size,
					abbr + "_item": replacement.item
			})
	vehicle_number = data.user
	# print(vehicle_number)
	user_details = frappe.db.sql(""" SELECT vd.license_plate as vehicle_no, vd.vehicle_brand as vehicle_brand, vd.vehicle_model as vehicle_model_name, vd.vehicle_type, 
								vd.tyre_change as tyre_change_km, vd.last_odometer_reading as odo_reading_kms, vd.alignment as free_alignment_kms, 
						 		cd.current_driver as driver_name, cd.mobile_no, cd.whatsapp as driver_whatsapp, cd.sms as driver_sms, cd.call as driver_call,
						 		cp.contact_person_name as contact_person, cp.contact_person_mobile as contact_mobile_no, cp.contact_person_email as email, cp.department as department, 
						 		cp.custom_whatsapp as contact_whatsapp, cp.custom_sms as contatct_sms, cp.custom_call as contact_call,
						 		cud.current_owner, cud.owner_mobile_no, cud.whatsapp as whatsapp, cud.call as `call`, cud.sms as sms, cud.owner_data as customer FROM `tabVehicle Details` as vd
						 		join `tabCurrent Driver` as cd on cd.parent = vd.name 
						 		join `tabCustomer Details` as cud on cud.license_plate = vd.name 
						 		join `tabContact Person` as cp on cp.parent = vd.name WHERE vd.license_plate = %s AND cd.primary = 1 AND cp.custom_primary = 1""", vehicle_number,as_dict = True)[0]
	val = frappe._dict(data.service)
	# print(val.alignment['lastAlignment'])
	
	air,nitrogen = False,False

	if val.inflation['type'] == 'air' :
		air = True
		nitrogen = False
	elif val.inflation['type'] == 'nitrogen' :
		air = False
		nitrogen = True
	else:
		air = False
		nitrogen = False
	
	service = {"alignment": val.Alignment, "rotation": val.Rotation, "oil_change": val.Oil_change, "balancing": val.Balancing, "inflation": val.Inflation,
				"ac_service": val.AcService, "battery": val.Battery, "wiper": val.Wiper, "car_wash": val.CarWash, "puncture": val.puncture, "tyre_edge" :val.tyre_edge,
				"tyre_patch": val.tyre_patch, "mushroom_patch": val.mashroom_patch, "last_alignment_kms": val.alignment['lastAlignment'], "next_alignment_kms": val.alignment['nextAlignment'],
				"rim": val.rotation['rim'], "wheel": val.rotation['wheel'], "oil_quality": val.oil_change['oil_quality'], "oil_quantity": val.oil_change['oil_quantity'], "front_left_gm": val.balancing['fl'],
				"front_right_gms": val.balancing['fr'], "rear_left_gms":val.balancing['bl'], "rear_right_gms":val.balancing['br'], "spare_tyre_gms": val.balancing['st'], "air": air, "nitrogen": nitrogen, "front_tyres_psi":val.inflation['ft'],
				"rear_tyres_psi": val.inflation['rt'], "ac_service_detail": val.ac, "wiper_detail": val.wiper, "battery_detail": val.battery, "car_wash_detail":val.car_wash   }
		

	doc = frappe.new_doc("Tyre Job Card")
	doc.update(five_point_checkup)
	doc.update(tyre_replacement)
	doc.update(user_details)
	doc.update(service)
	bills = [bill[0] for bill in data.bill]
	print(bills, "bills")
	billing_items = []
	total_amount = 0
	for items in bills:
		items = frappe._dict(items)
		total_amount += float(items.cost)
		billing_items.append({"item_code": items.itemCode, "warehouse": items.sourceWarehouse, "quantity" : items.requiredQuantity, "amount" : items.cost, "rate": items.rate})
	print(doc.as_dict(), "as_dict")
	doc.extend("billing_details", billing_items)

	doc.total_amount = total_amount
	doc.save(ignore_permissions=True)  # Save customer document
	print(doc.as_dict(), "as_dict")
	return {
		"status": 200,
		"message": "Jobcard Created Successfully"
	}

@frappe.whitelist(allow_guest=True)
def lead(**args):
	# print(args, type(args))
	data = frappe._dict(args)
	lead_user_details = {
		"first_name": data.current_owner,
		"mobile_no": data.owner_mobile_no,
		"custom_whatsapp": data.whatsapp,
		"custom_sms": data.sms,
		"custom_call": data.call,
	}

	doc = frappe.db.exists("Lead",{ "mobile_no" : data.owner_mobile_no})

	if doc:
		return {
			"status": 400,
			"message": "Lead Already Exists"
		}
	print( data.keys())
	services = frappe._dict(data["services"])

	service_details = {
		"custom_alignment": services.alignment,
		"custom_oil_change": services.oil_change,
		"custom_inflation": services.inflation,
		"custom_tyre_edge": services.tyre_edge,
		"custom_mushroom_patch": services.mushroom_patch,
		"custom_battery": services.battery,
		"custom_car_wash": services.car_wash,
		"custom_rotation": services.rotation,
		"custom_balancing": services.balancing,
		"custom_wiper": services.wiper,
		"custom_ac_service": services.ac_service,
		"custom_puncture": services.puncture,
		"custom_tyre_patch": services.tyre_patch,
	}

	doc = frappe.new_doc("Lead")
	doc.update(lead_user_details)
	doc.update(service_details)
	# items = frappe._dict(data["items"])
	# print(data.keys(), data["items"])
	for items_deatils in data.get("items"):
		items_deatils = frappe._dict(items_deatils)
		doc.append("custom_lead_items", {"brand": items_deatils.brand, "size": items_deatils.variants, "quantity" : items_deatils.quantity,"pattern": items_deatils.pattern,"tyre_type": items_deatils.type})
	doc.save(ignore_permissions=True)  # Save customer document
	return {
		"status": 200,
		"message": "Lead Created Successfully",
		"lead_item": doc.custom_lead_items,
		"total_amount": doc.custom_total_amount,
	}



@frappe.whitelist(allow_guest=True)
def lead_details(data):
	if frappe.db.get_value("Lead",{"mobile_no": data}):
		return frappe.get_doc("Lead", frappe.db.get_value("Lead",{"mobile_no": data})).as_dict()
	else:
		return {
			"status": 400,
			"message": "Lead Not Found"
		}
	

@frappe.whitelist(allow_guest=True)
def get_brand():
	return frappe.get_all("Brand", pluck="name")

@frappe.whitelist(allow_guest=True)
def get_size(brand):
	query = """
		SELECT DISTINCT bd.size, s.load_index, s.speed_rating
		FROM `tabBrand Details` AS bd
		JOIN `tabSize` AS s ON s.name = bd.size
		WHERE bd.parent = %(brand)s
	"""
	result = frappe.db.sql(query, {"brand": brand}, as_dict=True)
	if result:
		return result
	else:
		return {
			"status": 400,
			"message": "No Size Found"
		}

@frappe.whitelist(allow_guest=True)
def get_type(brand, size):
	results = frappe.get_all("Brand Details", {"parent": brand, "size": size}, ["tyer_type"])
	unique_types = set()
	for result in results:
		tyer_type = result.get("tyer_type")
		unique_types.add(tyer_type)
	if unique_types:
		return list(unique_types)
	else:
		return {
			"status": 400,
			"message": "No Type Found"
		}


@frappe.whitelist(allow_guest=True)
def get_pattern(brand, size, tyer_type):
	results = frappe.get_all("Brand Details", filters={"parent": brand, "size": size, "tyer_type": tyer_type}, fields=["pattern"])
	unique_patterns = set(result.get("pattern") for result in results)
	if unique_patterns :
		return list(unique_patterns)
	else :
		return {
			"status": 400,
			"message": "No Pattern Found"
		}

def create_service_items():
	List = ['Alignment','Rotation', 'Oil Change', 'Balancing', 'Inflation','Puncture','Tyre Edge', 'Tyre Patch','Mushroom Patch','Ac Service','Battery', 'Wiper','Car Wash']
	if frappe.db.exists("Brand",{ "name" : "Service"}):
		for row in List:
			if not frappe.db.exists("Item",{"item_name":row}):
				frappe.get_doc({
					"doctype": "Item",
                    "item_name": row,
                    "brand": "Service",
					"item_group":"Services",
					"stock_uom":"Nos",
					"item_code":row,
				}).insert(ignore_permissions=True)
	else:
		doc = frappe.get_doc(doctype = "Brand", brand = "Service")
		doc.insert(ignore_permissions=True)
		for row in List:
			if not frappe.db.exists("Item",{"item_name":row}):
				frappe.get_doc({
					"doctype": "Item",
                    "item_name": row,
                    "brand": "Service",
					"item_group":"Services",
					"stock_uom":"Nos",
					"item_code":row,
				}).insert(ignore_permissions=True)

@frappe.whitelist(allow_guest=True)
def get_ItemCode(brand, size, tyer_type,pattern):
	item_code = frappe.get_all("Brand Details", filters={"parent": brand, "size": size, "tyer_type": tyer_type, "pattern":pattern}, pluck="item_code")[0]
	return [item_code, get_item_rate(item_code)]
	
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
	if items_grouped_by_brand:
		return items_grouped_by_brand
	else:
		return {
			"status": 400,
			"message": "No Item Found"
		}
	
@frappe.whitelist(allow_guest=True)
def get_jobcard_details(searchJobCard):
    if searchJobCard:
        jobcard_details = frappe.get_all("Tyre Job Card",
                                          filters={'vehicle_no': searchJobCard},
                                          fields=["time_in", "name", "vehicle_no", "customer", "mobile_no"])
        if jobcard_details:
            return jobcard_details 
        else:
            return {
                "status": 400,
                "message": "No Job Card Found" 
            }
    else:
        job_card_details = frappe.get_all("Tyre Job Card",
                                           fields=["time_in", "name", "vehicle_no", "customer", "mobile_no"])
        return job_card_details 


@frappe.whitelist(allow_guest=True)
def get_enquiry_details(data):
	if data:
		doc = frappe.get_all("Lead", {"mobile_no": data},{"name","lead_name","mobile_no"})
		if doc:
			return doc
	else:
		doc = frappe.get_all("Lead", fields={"name", "lead_name", "mobile_no"})
		return doc

@frappe.whitelist(allow_guest=True)
def get_billing_details(name):
  doc = frappe.get_doc("Tyre Job Card", name)
  return {"billing_details":doc.billing_details, "total_amount": doc.total_amount}

@frappe.whitelist()
def get_item_rate(item_code):
	from erpnext.stock.report.item_price_stock.item_price_stock import get_item_price_qty_data
	price_list = get_item_price_qty_data({"item_code": item_code})
	if price_list:
		return price_list[0].selling_rate
	
	return 0

@frappe.whitelist()
def get_item(args):
	if isinstance(args, str):
		args = frappe._dict(json.loads(args))
	return frappe.db.get_value("Brand Details",{"parent": args.brand, "size": args.size, "tyer_type": args.tyre_type, "pattern": args.pattern}, "item_code")

@frappe.whitelist()
def get_warehouse():
	return frappe.get_all("Warehouse",{"is_group":0}, pluck="name")

def calculate_total_amount(self, method):
	if self.doctype == "Lead":
		total_amount = 0
		for row in self.custom_lead_items:
			item_code = get_item(frappe._dict({
												"brand": row.brand,
												"size": row.size,
												"pattern": row.pattern,
												"tyre_type": row.tyre_type
										}))

			self.custom_lead_items[row.idx - 1].rate = 0
			self.custom_lead_items[row.idx - 1].amount = 0
			if item_code:
				price_list = get_item_rate(item_code)
				# print(price_list)
				self.custom_lead_items[row.idx - 1].item_code = item_code
				self.custom_lead_items[row.idx - 1].rate = float(price_list)
				self.custom_lead_items[row.idx - 1].amount = int(row.quantity) * float(price_list)
				total_amount += self.custom_lead_items[row.idx - 1].amount


			self.custom_total_amount = total_amount

	if self.doctype == "Tyre Job Card":
		total_amount = 0
		for row in self.billing_details:
			self.billing_details[row.idx - 1].rate = 0
			self.billing_details[row.idx - 1].amount = 0
			if row.item_code:
				price_list = get_item_rate(row.item_code)
				print(price_list)
				self.billing_details[row.idx - 1].rate = price_list
				self.billing_details[row.idx - 1].amount = row.quantity * price_list
				total_amount += row.quantity * price_list


			self.total_amount = total_amount

@frappe.whitelist(allow_guest=True)
def delete_modified_customers(data):
    
	data = frappe._dict(data)
	if data.parentfield == "current_driver":
		doc_details = frappe.db.get_value("Current Driver", {"mobile_no": data.mobile_no}, ["name", "parent"], as_dict=True)
		if doc_details and doc_details.get('name') and doc_details.get('parent'):
			p_doc = frappe.get_doc("Customer Details", doc_details.get('parent'))
			for row in p_doc.current_driver:
				if row.name == doc_details.get('name'):
					p_doc.remove(row)
			p_doc.save()
	elif data.parentfield == "contact_person":
		doc_details = frappe.db.get_value("Contact Person", {"contact_person_mobile": data.contact_person_mobile}, ["name", "parent"], as_dict=True)
		if doc_details and doc_details.get('name') and doc_details.get('parent'):
			p_doc = frappe.get_doc("Customer Details", doc_details.get('parent'))  # Changed to "Contact" from "Contact Person"
			for row in p_doc.contact_person:  # Changed to "contact_person" from "current_driver"
				if row.name == doc_details.get('name'):
					p_doc.remove(row)
			p_doc.save()
	else:
		return {
			"status": 400,
			"message": "No Job Card Found"
	  	}
			


@frappe.whitelist()
def get_item(args):
	if isinstance(args, str):
		args = frappe._dict(json.loads(args))
	return frappe.db.get_value("Brand Details",{"parent": args.brand, "size": args.size, "tyer_type": args.tyre_type, "pattern": args.pattern}, "item_code")


@frappe.whitelist()
def get_item_rate(item_code):
	from erpnext.stock.report.item_price_stock.item_price_stock import get_item_price_qty_data
	price_list = get_item_price_qty_data({"item_code": item_code})
	if price_list:
		print(price_list)
		return price_list[0]["selling_rate"]
	
	return 0


@frappe.whitelist()
def get_warehouse():
	return frappe.get_all("Warehouse",{"is_group":0}, pluck="warehouse_name")

@frappe.whitelist()
def get_vehicleBrand():
    return frappe.get_all("Vehicle Brand",fields={"name"})

@frappe.whitelist()
def get_vehicleModel(model):
    return frappe.get_all("Vehicle Models", {"parent":model},"model")
