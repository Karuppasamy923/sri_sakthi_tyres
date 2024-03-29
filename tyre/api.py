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
               
                
            for contact_person in customer_details.contact_person:
                data= frappe.get_doc("ContactPerson",{"name":contact_person.contact_person_name})
                print(data.contact_person_name)
                contact_person.name=contact_person.contact_person_name
                contact_person.contact_person_name=data.contact_person_name
                            
            print(customer_details.current_owner)

        print("Vehicle Details:", vehicle_details)
        print("Customer Details:", customer_details)
        # print(customer_details.employee_name)

        if vehicle_details or customer_details :
            return [vehicle_details, customer_details]
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
        print(doc)
        doc.license_plate = license_plate
        print(doc.license_plate)
        doc.vehicle_brand = " ".join([w.capitalize() for w in data.get('vehicle_brand').split()]) if data.get('vehicle_brand') else None
        print(doc.vehicle_brand)
        doc.vehicle_model = " ".join([w.capitalize() for w in data.get('vehicle_model').split()]) if data.get('vehicle_model') else None
        print(doc.vehicle_model)
        doc.chassis_no = data.get('chassis_no').upper() if data.get('chassis_no') else None
        print(doc.chassis_no)
        doc.fuel_type = data.get('fuel_type')
        print(doc.fuel_type)
        doc.last_odometer_reading = data.get('last_odometer_reading')
        print(doc.last_odometer_reading)
        doc.alignment = data.get('alignment')
        print(doc.alignment)
        doc.tyre_change=data.get('tyre_change')
        print(doc.tyre_change)
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
        doc.current_owner = data.get('current_owner')
        doc.owner_mobile_no = data.get('owner_mobile_no')
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
                    new_driver.save(ignore_permissions=True)
                    driver = new_driver.name
                doc.append("current_driver", {"current_driver": driver, "mobile_no": driver_data.get('mobile_no')})
            else:
                cPerson = frappe.db.get_value("ContactPerson",{"contact_person_mobile":driver_data.get('mobile_no')})
                if not cPerson:
                    new_driver = frappe.new_doc("ContactPerson")
                    new_driver.contact_person_name=driver_data.get('driver_name')
                    new_driver.contact_person_mobile=driver_data.get('mobile_no')
                    new_driver.save(ignore_permissions=True)
                    cPerson = new_driver.name
                # Append new Contact Person document to the parent document
                doc.append("contact_person", {"contact_person_name": cPerson, "contact_person_mobile":driver_data.get('mobile_no')})

        # doc.save(ignore_permissions=True)  # Save customer document
        doc.save(ignore_permissions=True)
        frappe.db.commit()
        return ['',[doc]]


# function to create five point checkup
def create_five_point_checkup():
    pass

@frappe.whitelist(allow_guest=True)
def custom_test_api():
    data = {
        "msg": "This is test api"
    }

    return data