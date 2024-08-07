import frappe
import datetime
import json
import re
from erpnext.selling.doctype.sales_order.sales_order import make_sales_invoice
from erpnext.accounts.doctype.payment_entry.payment_entry import get_payment_entry

# function to get the vehicle & customer details (parameter = license plate)
@frappe.whitelist(allow_guest=True)
def get_details(license_plate):
    license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
    # regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
    # p = re.compile(regex)
    # regex = "^[A-Z]{2}[\\s-]{0,1}[0-9]{2}[\\s-]{0,1}[A-Z]{1,2}[\\s-]{0,1}[0-9]{4}$"
    # p = re.compile(regex)
    license_plate=license_plate.upper()
    if license_plate is None:
        return "NO Data Found!!!!"
    else:   
        if(len(license_plate)>=8 and len(license_plate)<=10):
            if license_plate:
                vehicle_details = ''
                customer_details = ''
                primary_details=[]
                customer =''

                # Check if Vehicle Details exist
                if frappe.db.exists("Vehicle Details", {"name": license_plate}):
                    vehicle_details = frappe.get_doc("Vehicle Details", {"name": license_plate})

                # Check if Customer Details exist
                if frappe.db.exists("Customer Details", {"name": license_plate}):
                    customer_details = frappe.get_doc("Customer Details", {"name": license_plate})
                    if customer_details.owner_data:
                        customer = frappe.get_doc("Customer",{"name":customer_details.owner_data})
                    for current_driver in customer_details.current_driver:
                        data= frappe.get_doc("Driver",{"name":current_driver.current_driver})
                        current_driver.name=current_driver.current_driver
                        current_driver.current_driver=data.full_name
                        if data.custom_primary:
                            primary_details.append(data)
               
                
                    for contact_person in customer_details.contact_person:
                        data= frappe.get_doc("ContactPerson",{"name":contact_person.contact_person_name})
                        contact_person.name=contact_person.contact_person_name
                        contact_person.contact_person_name=data.contact_person_name
                       
                        if data.custom_primary:
                            primary_details.append(data)
                            
                if vehicle_details or customer_details :
                    return [vehicle_details, customer_details,primary_details,customer]
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

@frappe.whitelist(allow_guest = True)
def exist_mobile_number(data):
    data = json.loads(data)
    mobile = data.get('mobile')
    owner = frappe.db.get_value("Customer",{"mobile_no":data.get('mobile')})
    if owner:
        return "mobileExist"
    

# function to store new customer details
@frappe.whitelist(allow_guest=True)
def store_customer_details(data):
    data = json.loads(data)
    license_plate = data.get('name').upper().replace(' ', '')
    license_plate = re.sub(r'[^a-zA-Z0-9]', '', license_plate)
    regex = "^[A-Z]{2}[0-9]{2}[A-Z]{1,2}[0-9]{4}$"
    p = re.compile(regex)

    if(re.search(p, license_plate)):
        if frappe.db.exists('Customer Details', {'name': license_plate}):
            doc=frappe.get_doc('Customer Details', {'name': license_plate})
            doc.license_plate = license_plate
            if frappe.db.exists("Customer",{'name':data.get('owner_data')}):
                owner = frappe.get_doc("Customer",data.get('owner_data'))
                owner.customer_name = data.get( 'current_owner')
                owner.custom_whatsapp = data.get('whatsapp')
                owner.custom_sms = data.get('sms')
                owner.custom_call = data.get('call')
                owner.custom_gstin=data.get('gst')
                owner.primary_address=data.get('address')
                owner.save(ignore_permissions=True)
                frappe.db.set_value('Customer', data.get('owner_data'),'mobile_no',data.get('owner_mobile_no'))
        
            #update a driver and conteact person
            new_driver = new_drivers = None
            for driver_data in data.get('employees', []):
                doc_type = driver_data.get('type')
                if doc_type == "current_driver":
                    driver = frappe.db.get_value("Driver",{"name":driver_data.get('name')})
                    # Append the name of the current_driver to the parent document
                    if not driver:
                        mobile_no = frappe.db.get_value("Driver",{"cell_number":driver_data.get('mobile_no')})
                        if not mobile_no:
                            new_driver = frappe.new_doc("Driver")
                            new_driver.full_name=driver_data.get('current_driver')
                            new_driver.cell_number=driver_data.get('mobile_no')
                            new_driver.custom_whatsapp_check=driver_data.get('whatsapp')
                            new_driver.custom_sms_check=driver_data.get('sms')
                            new_driver.custom_call_check=driver_data.get('call')
                            new_driver.custom_primary=driver_data.get('primary')
                            # new_driver.save(ignore_permissions=True)
                            # driver = new_driver.name
                            # doc.append("current_driver", {"current_driver": driver, "mobile_no": driver_data.get('mobile_no')})
                        else:
                            return "driver already exist"
                    else:
                        new_driver1=frappe.get_doc("Driver",{"name":driver_data.get('name')})
                        new_driver1.full_name=driver_data.get('current_driver')
                        new_driver1.cell_number=driver_data.get('mobile_no')
                        new_driver1.custom_whatsapp_check=driver_data.get('whatsapp')
                        new_driver1.custom_sms_check=driver_data.get('sms')
                        new_driver1.custom_call_check=driver_data.get('call')
                        if driver_data.get('primary')== True:
                            new_driver1.custom_primary=1
                        else:
                            new_driver1.custom_primary=0    
                        new_driver1.save(ignore_permissions=True)
                        # driver = new_driver.name  
                else:
                    cPerson = frappe.db.get_value("ContactPerson",{"name":driver_data.get('name')})
                    if not cPerson:
                        cPerson = frappe.db.get_value("ContactPerson",{"contact_person_mobile":driver_data.get('contact_person_mobile')})
                        if not cPerson:
                            new_drivers = frappe.new_doc("ContactPerson")
                            new_drivers.contact_person_name=driver_data.get('contact_person_name')
                            new_drivers.contact_person_mobile=driver_data.get('contact_person_mobile')
                            new_drivers.whatsapp=driver_data.get("custom_whatsapp")
                            new_drivers.sms=driver_data.get("custom_sms")
                            new_drivers.call=driver_data.get("custom_call")
                            new_drivers.custom_primary=driver_data.get('custom_primary')
                            # new_drivers.save(ignore_permissions=True)
                        else:
                            return "contact person already exist"
                    else:
                        new_driver2=frappe.get_doc("ContactPerson",{"name":driver_data.get('name')})
                        new_driver2.contact_person_name=driver_data.get('contact_person_name')
                        new_driver2.contact_person_mobile=driver_data.get('contact_person_mobile')
                        new_driver2.whatsapp=driver_data.get("custom_whatsapp")
                        new_driver2.sms=driver_data.get("custom_sms")
                        new_driver2.call=driver_data.get("custom_call")
                        # new_driver2.custom_primary=driver_data.get('primary')
                        if driver_data.get('custom_primary')== True:
                            new_driver2.custom_primary=1
                        else:
                            new_driver2.custom_primary=0
                        new_driver2.save(ignore_permissions=True)
                        # cPerson = new_driver.name 
                    # Append new Contact Person document to the parent document
                    #doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})
            if new_driver or new_drivers:
                if new_driver:
                    new_driver.save(ignore_permissions=True)
                    driver = new_driver.name
                    doc.append("current_driver", {"current_driver": driver, "mobile_no": driver_data.get('mobile_no')})
                if new_drivers:
                    new_drivers.save(ignore_permissions=True)
                    cPerson = new_drivers.name
                    doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile": driver_data.get('contact_person_mobile')})
            # doc.save(ignore_permissions=True)  # Save customer document
            doc.save(ignore_permissions=True)
            frappe.db.commit()
            return ['',[doc]]
        ##customer details doc not created then run this else 
        else:
            # New document in customer details
            doc = frappe.new_doc('Customer Details')
            doc.license_plate = license_plate
            owner = frappe.db.get_value("Customer", {"customer_name": data.get('current_owner'), "mobile_no": data.get('owner_mobile_no')})

            # Initialize new_owner
            new_owner = None

            # Check if owner data already exists
            if not owner and data.get("exists") == False:
                new_owner = frappe.new_doc("Customer")
                new_owner.customer_name = data.get('current_owner')
                new_owner.mobile_no = data.get('owner_mobile_no')
                new_owner.custom_whatsapp = data.get('whatsappChecked')
                new_owner.custom_sms = data.get('smsChecked')
                new_owner.custom_call = data.get('callChecked')
            elif owner and data.get("exists") == True:
                own = frappe.get_doc("Customer", owner)
                # own = frappe.get_doc("",owner)
                own.customer_name = data.get('current_owner')
                own.mobile_no = data.get('owner_mobile_no')
                own.custom_whatsapp = data.get('whatsappChecked')
                own.custom_sms = data.get('smsChecked')
                own.custom_call = data.get('callChecked')
            else:
                frappe.throw("Owner already exists with the given number: " + data.get('owner_mobile_no'))

            # Initialize variables for new driver and contact person
            new_driver = None
            new_drivers = None

            # Process driver and contact person data
            for driver_data in data.get('employees', []):
                doc_type = driver_data.get('type')
                if doc_type == "current_driver":
                    driver = frappe.db.get_value("Driver", {"cell_number": driver_data.get('mobile_no')})
                    if not driver:
                        if not new_driver:
                            new_driver = frappe.new_doc("Driver")
                        new_driver.full_name = driver_data.get('driver_name')
                        new_driver.cell_number = driver_data.get('mobile_no')
                        new_driver.custom_whatsapp_check = driver_data.get('whatsappChecked1')
                        new_driver.custom_sms_check = driver_data.get('smsChecked1')
                        new_driver.custom_call_check = driver_data.get('callChecked1')
                        new_driver.custom_primary = driver_data.get('primary')
                    else:
                        return "driver already exist"
                else:
                    cPerson = frappe.db.get_value("ContactPerson", {"contact_person_mobile": driver_data.get('mobile_no')})
                    if not cPerson:
                        if not new_drivers:
                            new_drivers = frappe.new_doc("ContactPerson")
                        new_drivers.contact_person_name = driver_data.get('driver_name')
                        new_drivers.contact_person_mobile = driver_data.get('mobile_no')
                        new_drivers.whatsapp = driver_data.get('whatsappChecked1')
                        new_drivers.sms = driver_data.get('smsChecked1')
                        new_drivers.call = driver_data.get('callChecked1')
                        new_drivers.custom_primary = driver_data.get('primary')
                    else:
                        return "contact person already exist"

            # Save the new owner, driver, and contact person data if they are new entries
            if new_owner or owner and (new_driver or new_drivers):
                if new_owner:
                    new_owner.save(ignore_permissions=True)
                    doc.owner_data = new_owner
                if owner:

                    own.save(ignore_permissions=True)    
                    doc.owner_data=own
                if new_driver:
                    new_driver.save(ignore_permissions=True)
                    doc.append("current_driver", {"current_driver": new_driver.name, "mobile_no": driver_data.get('mobile_no')})

                if new_drivers:
                    new_drivers.save(ignore_permissions=True)
                    doc.append("contact_person", {"contact_person_name": new_drivers.name, "contact_person_mobile": driver_data.get('mobile_no')})
                    
                # Save the customer data
                doc.save(ignore_permissions=True)
            elif new_owner:
                new_owner.save(ignore_permissions=True)
                doc.owner_data = new_owner
            else:
                own.save(ignore_permissions=True)
                doc.owner_data = own
                

            # Save the customer details document
            doc.save(ignore_permissions=True)
            frappe.db.commit()

            # doc.save(ignore_permissions=True)  # Save customer document

            doc.save(ignore_permissions=True)
            frappe.db.commit()
            return ['',[doc]]
    else:
        return "Enter a valid number"


# function to create job card
@frappe.whitelist(allow_guest=True)
def job_card(data,brand,model,company):
    data = frappe._dict(json.loads(data))
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
    tyre_replacement = user_details = {}
    tyre_types = {"Front Left": "fl", "Front Right": "fr", "Rear Left": "rl", "Rear Right": "rr", "Spare Tyre": "sp"}
    for replacement in data.replace:
        replacement = frappe._dict(replacement)
        if replacement.type :
            abbr = tyre_types[replacement.type]
            tyre_replacement.update({
                    abbr + "_brand": replacement.brand,
                    abbr + "_load_index": replacement.dot,	
                    abbr + "_pattern": replacement.pattern,
                    abbr + "_speed_rating": replacement.speedRating,
                    abbr + "_tt_tl": replacement.ttTl,
                    abbr + "_size": replacement.size,
                    abbr + "_item": replacement.item,
                    abbr + "_warranty": replacement.warranty,
                    abbr + "_max_years": replacement.maxYears,
            })
    vehicle_number = data.user
    user_details = frappe.db.sql(""" 
                                    SELECT vd.license_plate as vehicle_no,
                                        vd.vehicle_brand as vehicle_brand,
                                        vd.vehicle_model as vehicle_model_name,
                                        vd.vehicle_type,
                                        vd.tyre_change as tyre_change_km,
                                        vd.last_odometer_reading as odo_reading_kms,
                                        vd.alignment as free_alignment_kms,
                                        COALESCE(cd.current_driver, cp.contact_person_name) as name,
                                        COALESCE(cd.mobile_no, cp.contact_person_mobile, cud.owner_mobile_no) as mobile_no,
                                        COALESCE(cd.whatsapp, cp.custom_whatsapp, cud.whatsapp) as whatsapp,
                                        COALESCE(cd.sms, cp.custom_sms, cud.sms) as sms,
                                        COALESCE(cd.`call`, cp.custom_call, cud.`call`) as `call`,
                                        cp.contact_person_email as email,
                                        cp.department as department,
                                        cud.current_owner,
                                        cud.owner_data as customer
                                    FROM `tabVehicle Details` as vd
                                    LEFT JOIN `tabCurrent Driver` as cd ON cd.parent = vd.name
                                    LEFT JOIN `tabCustomer Details` as cud ON cud.license_plate = vd.name 
                                    LEFT JOIN `tabContact Person` as cp ON cp.parent = vd.name
                                    WHERE vd.license_plate = '{0}' 
                                        AND (cd.current_driver IS NOT NULL OR cp.contact_person_name IS NOT NULL OR cud.owner_data IS NOT NULL)
                                    """.format(vehicle_number), as_dict=True)





    if user_details:
        user_details = user_details[0]
    else:
        user_details = {}
    val = frappe._dict(data.service)    
    
    air,nitrogen = False,False

    if val.inflations['type'] == 'air' :
        air = True
        nitrogen = False
    elif val.inflations['type'] == 'nitrogen' :
        air = False
        nitrogen = True
    else:
        air = False
        nitrogen = False
    
    service = {"alignment": val.Alignment, "rotation": val.Rotation, "oil_change": val.Oil_change, "balancing": val.Balancing, "inflation": val.Inflation,
                "ac_service": val.AcService, "battery": val.Battery, "wiper": val.Wiper, "car_wash": val.CarWash, "puncture": val.Puncture, "tyre_edge" :val.TyreEdge,
                "tyre_patch": val.TyrePatch, "mushroom_patch": val.MushroomPatch, "last_alignment_kms": val.alignments['lastAlignment'], "next_alignment_kms": val.alignments['nextAlignment'],
                "rim": val.rotations['inche'], "wheel": val.rotations['wheel_count'], "oil_quality": val.oil_changes['oil_quality'], "oil_quantity": val.oil_changes['oil_quantity'],"custom_inches":val.balancings['inches'],"custom_type":val.balancings['type'],"custom_grams_check":val.balancings['gramsCheck'], "front_left_gm": val.balancings['fl'],
                "front_right_gms": val.balancings['fr'], "rear_left_gms":val.balancings['bl'], "rear_right_gms":val.balancings['br'], "spare_tyre_gms": val.balancings['st'], "air": air, "nitrogen": nitrogen, "front_tyres_psi":val.inflations['ft'],
                "rear_tyres_psi": val.inflations['rt'], "ac_service_detail": val.ac, "wiper_detail": val.wiper, "battery_detail": val.battery, "car_wash_detail":val.car_wash   }
        
    doc = frappe.new_doc("Tyre Job Card")
    doc.update(five_point_checkup)
    doc.update(tyre_replacement)
    doc.update(user_details)
    doc.update(service)
    bills = [bill[0] for bill in data.bill]
    billing_items = []
    total_amount = 0
    for items in bills:
        items = frappe._dict(items)
        total_amount += float(items.cost)
        billing_items.append({"item_code": items.itemCode, "warehouse": items.sourceWarehouse, "quantity" : items.requiredQuantity, "amount" : items.cost, "rate": items.rate, "warranty":items.warranty, "max_years":maxyears(items.warranty), "additional":items.additional})
    doc.extend("billing_details", billing_items)

    doc.total_amount = total_amount
    doc.save(ignore_permissions=True)  # Save customer document
    sales_order(bills,user_details.customer,company)
    return {
        "status": 200,
        "message": "Jobcard Created Successfully",
        "datas":tyre_replacement
    }
    
from datetime import datetime
def maxyears(warranty):
    try:
        warranty_years = float(warranty)
        if warranty_years == 0:
            return None
    except ValueError:
        return None
    
    today = datetime.today()
    expiry_date = datetime(today.year + int(warranty_years), today.month, today.day)
    month = expiry_date.strftime('%m')
    day = expiry_date.strftime('%d')
    year = expiry_date.strftime('%Y')
    max_years = f"{month}_{day}_{year}"
    send_years = f"{year}-{month}-{day}"

    return send_years

@frappe.whitelist(allow_guest=True)
def lead(**args):
    data = frappe._dict(args)
    lead_user_details = {
        "first_name": data.current_owner,
        "mobile_no": data.owner_mobile_no,
        "custom_vehicle_brand":data.vehicle_brand,
        "custom_vehicle_model":data.vehicle_model,
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
    # l=['Alignment','Oil_change','Inflation','tyre_edge','mushroom_patch','Battery','CarWash','Rotation','Balancing','Wiper','AcService','puncture','tyre_patch']
 
    service_list = ['Alignment','Oil_change','Inflation','tyre_edge','mushroom_patch','Battery','CarWash','Rotation','Balancing','Wiper','AcService','puncture','tyre_patch']
    service_dict = {key: service for service, key in zip(service_list, service_details.keys())}
  
    doc = frappe.new_doc("Lead")
    doc.update(lead_user_details)
    doc.update(service_details)
    for service, value in service_details.items():
        if value:
            for Services, values in service_dict.items():
                if service == Services :
                    doc.append("custom_lead_items",{"item_code":values,"quantity" : 1})

    for items_deatils in data.get("items"):
        items_deatils = frappe._dict(items_deatils)
        doc.append("custom_lead_items", {"brand": items_deatils.brand, "size": items_deatils.variants, "quantity" : items_deatils.quantity,"pattern": items_deatils.pattern,"tyre_type": items_deatils.type})
    doc.save(ignore_permissions=True)  # Save customer document
    return {
        "status": 200,
        "message": "Lead Created Successfully",
        "lead_item": doc.custom_lead_items,
        "total_amount": doc.custom_total_amount,
        "name":doc.name
    }

@frappe.whitelist(allow_guest=True)
def delete_lead(data):
    frappe.delete_doc("Lead",data)
    return{
        "status": 200,
        "message": "Lead Deleted"
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
    doc =  frappe.get_all("Brand", pluck="name")
    brand = []
    for row in doc:
        if row != "Service":
            brand.append(row)
    return brand

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
def get_type(brand, size, pattern):
    results = frappe.get_all("Brand Details", {"parent": brand, "size": size, "pattern":pattern}, ["tyer_type"])
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
def get_pattern(brand, size):
    results = frappe.get_all("Brand Details", filters={"parent": brand, "size": size}, fields=["pattern"])
    unique_patterns = set(result.get("pattern") for result in results)
    if unique_patterns :
        return list(unique_patterns)
    else :
        return {
            "status": 400,
            "message": "No Pattern Found"
        }

def create_service_items():
    List = ['Alignment','Rotation', 'Oil_change', 'Balancing', 'Inflation','puncture','tyre_edge', 'tyre_patch','mushroom_patch','AcService','Battery', 'Wiper','CarWash']
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
    brand=None
    model=None
    inch=None
    type=None
    return [item_code, get_item_rate(item_code,brand,model,inch,type)]
    
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
            for job_card in job_card_details:
                customer_details = frappe.get_all("Customer", fields=["customer_name", "name"], filters={'name': job_card['customer']})        
                if customer_details:
                    customer_detail = customer_details[0]
                    if customer_detail['name'] == job_card['customer']:
                        job_card["customer_name"] = customer_detail['customer_name']
            return jobcard_details 
        else:
            return {
                "status": 400,
                "message": "No Job Card Found" 
            }
    else:
        job_card_details = frappe.get_all("Tyre Job Card",
                                           fields=["time_in", "name", "vehicle_no", "customer", "mobile_no"])
        for job_card in job_card_details:
            customer_details = frappe.get_all("Customer", fields=["customer_name", "name"], filters={'name': job_card['customer']})        
            if customer_details:
                customer_detail = customer_details[0]
                if customer_detail['name'] == job_card['customer']:
                    job_card["customer_name"] = customer_detail['customer_name']
        return job_card_details 


@frappe.whitelist(allow_guest = True)
def delete_vehicle(data):
    data = json.loads(data)
    license_plate = data.get('name').upper().replace(' ', '')
    if frappe.db.exists("Vehicle Details", {"name": license_plate}):
        vehicle_details = frappe.get_doc("Vehicle Details", license_plate)
        frappe.delete_doc("Vehicle Details", license_plate, force=True)
        if frappe.db.exists("Customer Details", {"name": license_plate}):
            customer_details = frappe.get_doc("Customer Details", license_plate).as_dict()

            # Check if there are any linked Tyre Job Cards
            tyre_job_cards = frappe.get_all("Tyre Job Card", filters={"vehicle_no": customer_details["name"]})
            if tyre_job_cards:
                for tyre_job_card in tyre_job_cards:
                    frappe.delete_doc("Tyre Job Card", tyre_job_card.name, force=True)

            # Delete linked Driver documents
            for driver in customer_details.get("current_driver", []):
                if frappe.db.exists("Driver", {"cell_number": driver.mobile_no}):
                    driver_details = frappe.get_doc("Driver", {"cell_number": driver.mobile_no})
                    frappe.delete_doc("Driver", driver_details.name, force=True)
                else:
                    print("Driver with mobile number {} not found. Skipping deletion.".format(driver.mobile_no))

            # Delete linked Contact Person documents
            for contact_person in customer_details.get("contact_person", []):
                if frappe.db.exists("ContactPerson", {"contact_person_mobile": contact_person.contact_person_mobile}):
                    contact_person_details = frappe.get_doc("ContactPerson", {"contact_person_mobile": contact_person.contact_person_mobile})
                    frappe.delete_doc("ContactPerson", contact_person_details.name, force=True)
                    print("Deleted Contact Person with mobile number:", contact_person.contact_person_mobile)
                else:
                    print('Contact Person with mobile number {} not found. Skipping deletion.'.format(contact_person.contact_person_mobile))

            # Delete the Customer Details document
            frappe.delete_doc("Customer Details", license_plate, force=True)

            # Check if there's an original Customer linked and delete it
            if frappe.db.exists("Customer", {"mobile_no": customer_details.owner_mobile_no}):
                original_customer = frappe.get_doc("Customer", {"mobile_no": customer_details.owner_mobile_no})
                frappe.delete_doc("Customer", original_customer.name)
                print("Deleted original customer:", customer_details.owner_mobile_no)
            else:
                print("Original Customer not found.")
            return "deleted"
    return "deleted"


    
@frappe.whitelist(allow_guest=True)
def get_enquiry_details(data):
    if data:
        return frappe.get_all("Lead", {"mobile_no": data},{"name","lead_name","mobile_no"})
    else:
        return frappe.get_all("Lead", fields={"name", "lead_name", "mobile_no"})


@frappe.whitelist(allow_guest=True)
def get_billing_details(name):
    doc = frappe.get_doc("Tyre Job Card", name)
    billing_details = []
    
    for billing_detail in doc.billing_details:
        billing_details.append({
            "item_code": billing_detail.item_code,
            "quantity": billing_detail.quantity,
            "rate": billing_detail.rate,
            "amount": billing_detail.amount,
            "warehouse": billing_detail.warehouse,
            "warranty": billing_detail.warranty,
            "max_years": billing_detail.max_years,
            "additional":billing_detail.additional
        })    
    return {
        "billing_details": billing_details,
        "total_amount": doc.total_amount,
    }
    
@frappe.whitelist(allow_guest=True)
def get_enquiry(name):
    doc = frappe.get_doc("Lead", name)
    lead_items = []
    for i in doc.custom_lead_items:
        lead_items.append(i.as_dict())
    return {"enquiry_details":lead_items, "total_amount": doc.custom_total_amount, "vehicle_brand":doc.custom_vehicle_brand, "vehicle_model":doc.custom_vehicle_model}

@frappe.whitelist(allow_guest=True)
def get_item_rate(item_code,brand,model,inch,type):
    if inch:
        if item_code == "Rotation":
            doc = frappe.get_all("Tyre Edge Rotation Price", filters={"name": inch}, fields=["price"])
            return doc[0].price
        if item_code == "Balancing" and type:
            doc = frappe.get_all("Wheel Balancing", filters={"inche": inch,"type":type}, fields=["price"])
            return doc[0].price
    
    doc = frappe.get_all("Vehicle Model Item Price", filters={'parent':model, "item":item_code}, fields={'price'})
    if doc:
        return doc[0].price
    
    from erpnext.stock.report.item_price_stock.item_price_stock import get_item_price_qty_data
    price_list = get_item_price_qty_data({"item_code": item_code})
    if price_list:
        return price_list[0]["selling_rate"]
    
    return 0

@frappe.whitelist()
def get_item(args):
    if isinstance(args, str):
        args = frappe._dict(json.loads(args))
    return frappe.db.get_value("Brand Details",{"parent": args.brand, "size": args.size, "tyer_type": args.tyre_type, "pattern": args.pattern}, "item_code")

# @frappe.whitelist()
# def get_warehouse(company):
#     return frappe.get_all("Warehouse",filters={"is_group": 0,"company": company}, pluck="name")


@frappe.whitelist()
def get_Company():
     return frappe.get_all("Company",pluck="name")

def calculate_total_amount(self, method):
    model = None
    brand = None
    inch = None
    type = None
    if self.doctype == "Lead":
        total_amount = 0
        for row in self.custom_lead_items:
            if row.item_code:
                price_list = get_item_rate(row.item_code,brand,model,inch,type)
                self.custom_lead_items[row.idx - 1].rate = float(price_list)
                self.custom_lead_items[row.idx - 1].amount =int(row.quantity)* float(price_list)
                total_amount += self.custom_lead_items[row.idx - 1].amount
            else:    
                item_code = get_item(frappe._dict({
                                                    "brand": row.brand,
                                                    "size": row.size,
                                                    "pattern": row.pattern,
                                                    "tyre_type": row.tyre_type
                                            }))

                self.custom_lead_items[row.idx - 1].rate = 0
                self.custom_lead_items[row.idx - 1].amount = 0
                if item_code:
                    price_list = get_item_rate(item_code,brand,model,inch,type)
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
                price_list = get_item_rate(row.item_code,brand,model)
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


# @frappe.whitelist()
# def get_item_rate(item_code):
# 	from erpnext.stock.report.item_price_stock.item_price_stock import get_item_price_qty_data
# 	price_list = get_item_price_qty_data({"item_code": item_code})
# 	if price_list:
# 		return price_list[0]["selling_rate"]
    
# 	return 0


@frappe.whitelist()
def get_warehouse(company):
    print(company, "**************")
    return frappe.get_all("Warehouse", filters={"company": company, "is_group": 0}, pluck="warehouse_name")


@frappe.whitelist()
def get_vehicleBrand():
    return frappe.get_all("Vehicle Brand",fields={"name"})

@frappe.whitelist()
def get_vehicleModel(model):
    return frappe.get_all("Vehicle Models", {"parent":model},"model")

from datetime import datetime
@frappe.whitelist(allow_guest=True)
def send_quotation(data):
    import json
    import frappe
    import requests
    url = "https://graph.facebook.com/v17.0/312918851895922/messages"
    try:
        data = json.loads(data)
        mobile = data.get('mobile_no')
        license_plate = data.get('license_plate')
        doc = ""
        enquiry = ""
        if mobile and license_plate:
            doc = frappe.get_doc("Tyre Job Card", {"vehicle_no": license_plate})
        elif mobile and not license_plate:
            enquiry = frappe.get_doc("Lead",{"mobile_no":mobile})
        # job_card_detail = doc.as_dict()
        # def convert_to_dict(obj):
        # 	if isinstance(obj, datetime):
        # 		return obj.strftime("%Y-%m-%d %H:%M:%S")
        # 	elif isinstance(obj, dict):
        # 		return {k: convert_to_dict(v) for k, v in obj.items()}
        # 	elif isinstance(obj, list):
        # 		return [convert_to_dict(elem) for elem in obj]
        # 	else:
        # 		return obj

        # doc_serializable = convert_to_dict(doc.as_dict())
        # doc_json = json.dumps(doc_serializable)
        if doc:
            docs = frappe.get_doc("Customer Details",{"name":license_plate}).as_dict()
            headers = {
                'Authorization':'Bearer EAAPvJMkEALEBO6dcBS0YuNy5Iq6gftR6hjykaMgrYBMlsVQIRc9ZCub7cQnXE52GfWTkOkAcOFOCPF2zod2NFvkjGOjKDgC7rL7PvPk36aC49tii1TDq2HjoBlz44MZCcKnm3WHxRBlX4NuJpM6S1oisCA5FVk7pnDGGIojE6QZCk8fnnxBRiOLDBvtZAaiN',
                'Content-Type': 'application/json'
            }
            payload = json.dumps({
                    "messaging_product": "whatsapp",
                    "to": "91"+mobile,
                    "type": "template",
                    "template": {
                        "name": "job_card_quotation",
                        "language": {
                            "code": "en_us"
                        },
                        "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": docs.current_owner
                                },
                                {
                                    "type": "text",
                                    "text": docs.first_name
                                },
                                {
                                    "type": "text",
                                    "text": doc.total_amount
                                }
                            ]
                        },
                        {
                            "type":"button",
                            "sub_type":"url",
                            "index":0,
                            "parameters":[
                                {
                                    "type":"text",
                                    "text":f"{frappe.utils.get_site_url(frappe.local.site)}/api/method/frappe.utils.print_format.download_pdf?doctype=Tyre%20Job%20Card&name={doc.name}&format=Standard&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en"
                                }
                            ]
                        }
                    ]
                }
            })
            response = requests.request("POST",url, headers=headers, data=payload)
            return "success"

        if enquiry:
            headers = {
                'Authorization':'Bearer EAAPvJMkEALEBO6dcBS0YuNy5Iq6gftR6hjykaMgrYBMlsVQIRc9ZCub7cQnXE52GfWTkOkAcOFOCPF2zod2NFvkjGOjKDgC7rL7PvPk36aC49tii1TDq2HjoBlz44MZCcKnm3WHxRBlX4NuJpM6S1oisCA5FVk7pnDGGIojE6QZCk8fnnxBRiOLDBvtZAaiN',
                'Content-Type': 'application/json'
            }
            payload = json.dumps({
                "messaging_product": "whatsapp",
                    "to": "91"+mobile,
                    "type": "template",
                    "template": {
                        "name": "job_card_quotation",
                        "language": {
                            "code": "en_us"
                        },
                        "components": [
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": enquiry.first_name
                                },
                                {
                                    "type": "text",
                                    "text": enquiry.name
                                },
                                {
                                    "type": "text",
                                    "text": enquiry.custom_total_amount
                                }
                            ]
                        },
                        {
                            "type":"button",
                            "sub_type":"url",
                            "index":0,
                            "parameters":[
                                {
                                    "type":"text",
                                    "text":f"{frappe.utils.get_site_url(frappe.local.site)}/api/method/frappe.utils.print_format.download_pdf?doctype=Lead&name={enquiry.name}&format=Standard&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en"
                                }
                            ]
                        }
                    ]
                }
            })
            response = requests.request("POST",url, headers=headers, data=payload)
        else:
            return "lead details not found"
    except Exception as e:
        return "Error occurred: " + str(e)


@frappe.whitelist()
def get_customer(data):
    if data.isdigit():
        # Search for the customer by partial match of mobile number
        customers = frappe.get_all(
            "Customer", 
            fields=["name", "customer_name", "mobile_no", "custom_whatsapp", "custom_sms", "custom_call"], 
            filters={"mobile_no": ("like", f"%{data}%")}
        )
    else:
        # Search for the customer by name
        customers = frappe.get_all(
            "Customer", 
            fields=["name", "customer_name", "mobile_no", "custom_whatsapp", "custom_sms", "custom_call"], 
            filters={"customer_name": ("like", f"%{data}%")}
        )
    
    customer_details = [{
        "name": customer.name,
        "customer_name": customer.customer_name,
        "mobile_no": customer.mobile_no,
        "custom_whatsapp": customer.custom_whatsapp,
        "custom_sms": customer.custom_sms,
        "custom_call": customer.custom_call
    } for customer in customers]
    
    if not customer_details:
        return [{"message": "No data found"}]
    
    return customer_details



@frappe.whitelist()
def get_items(item_group=None):
    items = frappe.get_all("Item", filters={"has_variants": 0})
    return items

@frappe.whitelist()
def create_customer(name, no,gs,add,what,call,sms):
    
    if what == False or call==False or sms==False:
        return "Fill the require field"
    # Validate mobile number
    if not add:
        return "Error: Fill the Address Field"
    if not no.isdigit() or len(no) != 10:
        return "Error: Mobile number must be a 10-digit number"
    
    regex = "^[0-9]{2}[A-Z]{5}[0-9]{4}"+"[A-Z]{1}[1-9A-Z]{1}"+"Z[0-9A-Z]{1}$"
     
    # Compile the ReGex
    p = re.compile(regex)
    
    
    if gs :
        if not re.search(p, gs):
            return "Error: Enter a correct GSTIN number!"

    
    number = frappe.get_all("Customer", filters={"mobile_no": no})
    if number:
        return "Mobile number is already exists!"
    else :
        # Convert name to first letter capitalized
        
        name = name.strip().capitalize()
        doc=frappe.new_doc("Customer")
        doc.customer_name=name
        doc.mobile_no=no
        doc.primary_address=add
        doc.custom_gstin=gs
        doc.custom_whatsapp=what
        doc.custom_call=call
        doc.custom_sms=sms
        doc.save(ignore_permissions=True)
        return "Customer created successfully"

@frappe.whitelist()
def sales_order(data, name,company):
    # Deserialize the data if it's a JSON string
    if isinstance(data, str):
        data = json.loads(data)

    # Create a new Sales Order document
    doc = frappe.new_doc("Sales Order")
    doc.customer = name
    doc.company = company

    current_date = datetime.now().date()
    # Iterate over the data to add items to the Sales Order
    for sublist in data:
        if str(type(sublist))=="<class 'list'>":
            sublist=sublist[0]
        doc.append("items", {
                        'item_code': sublist['itemCode'],
                        'warehouse':frappe.db.get_value('Warehouse',{'warehouse_name':sublist['sourceWarehouse'],'company':doc.company},"name"),
                        'qty': sublist['requiredQuantity'],
                        'delivery_date':  current_date,
                        'rate':sublist['rate']
                    })

    # Save the document
    doc.save(ignore_permissions=True)
    # doc.submit()
    # si_doc=make_sales_invoice(source_name=doc.name)
    # si_doc.save(ignore_permissions=True)
    # si_doc.submit()
    # # pay_invoice(si_doc.name)
    return "done"

@frappe.whitelist()
def get_inch_list():
    items = frappe.get_all("Tyre Edge Rotation Price", fields=["name"])
    inch_list = [item['name'] for item in items]
    inch_list.sort()
    
    return inch_list


@frappe.whitelist()
def get_permission():
    permission = frappe.get_single("Price changing permission")
    return permission.allow_permission
    
# @frappe.whitelist()
# def pay_invoice(name):
#     pay_doc=get_payment_entry(dt="Sales Invoice",dn=name)
    
#     pay_doc.mode_of_payment="Cash"
#     pay_doc.save(ignore_permissions=True)
#     pay_doc.submit()
    
@frappe.whitelist()
def send_invoice_via_whatsapp(doctype, name, print_format, letterhead):
    from frappe.utils.file_manager import save_file
    import requests
    import json
    try:
        doc = frappe.get_doc(doctype, name)
        print_doc = frappe.get_doc("Print Page Settings", "Print Page Settings")
        mobile_number = frappe.db.get_value(doctype, name, "mobile_no")
        if mobile_number:
            return
        pdf = frappe.get_print(doctype=doctype, name=name, print_format=print_format,as_pdf=True, no_letterhead=0, letterhead=letterhead)
        file = save_file("{0}.pdf".format(name), pdf ,None ,None ,is_private=0 ,folder="Home")
        file_url = file.file_url
        url = "https://graph.facebook.com/v17.0/{0}/messages".format(print_doc.whatsapp_id)

        payload = json.dumps({
        "messaging_product": "whatsapp",
        "to": mobile_number,
        "type": "template",
        "template": {
            "name": print_doc.sales_invoice_template,
            "language": {
            "code": "en_us"
            },
            "components": [
            {
                "type": "body",
                "parameters": [
                {
                    "type": "text",
                    "text": doc.customer
                },
                {
                    "type": "text",
                    "text": doc.name
                },
                {
                    "type": "text",
                    "text": doc.grand_total
                }
                ]
            },
            {
                "type": "button",
                "sub_type": "url",
                "index": 0,
                "parameters": [
                {
                    "type": "text",
                    "text": file_url
                }
                ]
            }
            ]
        }
        })
        headers = {
        'Authorization': 'Bearer {0}'.format(print_doc.bearer_token),
        'Content-Type': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload)
        frappe.log_error(response.text)
    except Exception as e:
        frappe.log_error(title="Whatsapp API Error", message="Invoice No: {0}\n".format(name)+str(e))

def send_invoice(self, method):
    send_invoice_via_whatsapp(self.doctype, self.name, "New Sales Invoice", "Sri Sakthi Tyres")
    


    