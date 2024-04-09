import frappe
import datetime
import json

# function to get the vehicle & customer details (parameter = license plate)
@frappe.whitelist(allow_guest=True)
def get_details(license_plate):
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


# function to store new vehicle details
@frappe.whitelist(allow_guest=True)
def store_vehicle_details(data):
    data = json.loads(data)
    license_plate = data.get('name').upper().replace(' ', '')
    print(license_plate)
    
    # checking if vehicle number already exists
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
        
    # # not in FE
    #     # doc.wheel

    # doc.save(ignore_permissions=True)

# function to store new customer details
@frappe.whitelist(allow_guest=True)
def store_customer_details(data):
    data = json.loads(data)
    print(data)
    license_plate = data.get('name').upper().replace(' ', '')
    print(license_plate)

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
                # doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})

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
                    new_driver.contact_person_name=driver_data.get('driver_name')
                    new_driver.contact_person_mobile=driver_data.get('mobile_no')
                    new_driver.whatsapp=driver_data.get('whatsappChecked1')
                    new_driver.sms=driver_data.get('smsChecked1')
                    new_driver.call=driver_data.get('callChecked1')
                    new_driver.custom_primary=driver_data.get('custom_primary')
                    new_driver.save(ignore_permissions=True)
                    cPerson = new_driver.name
                # Append new Contact Person document to the parent document
                doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})

        # doc.save(ignore_permissions=True)  # Save customer document
        doc.save(ignore_permissions=True)
        frappe.db.commit()
        return ['',[doc]]


# function to create job card
@frappe.whitelist(allow_guest=True)
def job_card(data):
    data = json.loads(data)
    print(data)
    doc=frappe.new_doc("Tyre Job Card")
    doc.alignment=data.get("Alignment")
    doc.rotation=data.get("Rotation")
    doc.oil_change=data.get("Oil_change")
    doc.balancing=data.get("Balancing")
    doc.inflation=data.get("Inflation")
    doc.ac_service=data.get("AcService")
    doc.battery=data.get("Battery")
    doc.wiper=data.get("Wiper")
    doc.car_wash=data.get("CarWash")
    doc.puncture=data.get("puncture")
    doc.tyre_edge=data.get("tyre_edge")
    doc.tyre_patch=data.get("tyre_patch")
    doc.mushroom_patch=data.get("mashroom_patch")
    doc.last_alignment_kms=data["alignment"].get("lastAlignment")
    doc.next_alignment_kms=data["alignment"].get("nextAlignment")
    doc.rim=data["rotation"].get("rim")
    doc.wheel=data["rotation"].get("wheel")
    doc.oil_quality=data["oil_change"].get("oil_quality")
    doc.oil_quantity=data["oil_change"].get("oil_quantity")
    doc.front_left_gm=data["balancing"].get("fl")
    doc.front_right_gms=data["balancing"].get("fr")
    doc.rear_left_gms=data["balancing"].get("bl")
    doc.rear_right_gms=data["balancing"].get("br")
    doc.spare_tyre_gms=data["balancing"].get("st")
    print(data["inflation"].get("type"))
    if data["inflation"].get("type")=='air':
        doc.air=1
    if data["inflation"].get("type")=='nitrogen':
        doc.nitrogen=1
    doc.front_tyres_psi=data["inflation"].get("ft")
    doc.rear_tyres_psi=data["inflation"].get("rt")
    doc.ac_service_detail=data.get("ac")
    doc.battery_detail=data.get("battery")
    doc.wiper_detail=data.get("wiper")
    doc.car_wash_detail=data.get("car_wash")
    doc.save(ignore_permissions=True)
    print(doc)
