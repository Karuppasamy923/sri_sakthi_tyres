app_name = "tyre"
app_title = "Tyre"
app_publisher = "krishna@aerele.in"
app_description = "Custom app for Digityre"
app_email = "krishna@aerele.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tyre/css/tyre.css"
# app_include_js = "/assets/tyre/js/tyre.js"

# include js, css files in header of web template
# web_include_css = "/assets/tyre/css/tyre.css"
# web_include_js = "/assets/tyre/js/tyre.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tyre/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tyre/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tyre.utils.jinja_methods",
# 	"filters": "tyre.utils.jinja_filters"
# }

# Installation
# ------------

after_migrate = "tyre.api.create_service_items"
# before_install = "tyre.install.before_install"
# after_install = "tyre.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tyre.uninstall.before_uninstall"
# after_uninstall = "tyre.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tyre.utils.before_app_install"
# after_app_install = "tyre.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tyre.utils.before_app_uninstall"
# after_app_uninstall = "tyre.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tyre.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Lead": {
		"validate": "tyre.api.calculate_total_amount",
	},
	# "Tyre Job Card": {
	# 	"validate": "tyre.api.calculate_total_amount",
	# }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tyre.tasks.all"
# 	],
# 	"daily": [
# 		"tyre.tasks.daily"
# 	],
# 	"hourly": [
# 		"tyre.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tyre.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tyre.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tyre.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tyre.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tyre.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tyre.utils.before_request"]
# after_request = ["tyre.utils.after_request"]

# Job Events
# ----------
# before_job = ["tyre.utils.before_job"]
# after_job = ["tyre.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tyre.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'}, {'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]

whitelist = ["GET", "POST"]

app_list = ['get_details','store_vehicle_details','job_card', 'stock_details','get_brand','get_size','get_pattern','get_type','get_ItemCode','get_jobcard_details','delete_vehicle','get_enquiry_details']

from tyre.api import get_details, store_vehicle_details, job_card, stock_details,get_brand,get_size,get_pattern,get_type,get_ItemCode,get_jobcard_details,delete_vehicle, get_enquiry_details, exist_mobile_number,send_quotation,get_enquiry

api_routes = {
    "GET": {
        "/api/method/tyre.api.store_vehicle_details": store_vehicle_details,
        "/api/method/tyre.api.stock_details":stock_details,
        "/api/method/tyre.api.get_brand":get_brand,
        "/api/method/tyre.api.get_jobcard_details":get_jobcard_details,
        "/api/method/tyre.api.get_enquiry_details":get_enquiry_details,
        "/api/method/tyre.api.get_enquiry":get_enquiry,
    },
    "POST": {
        "/api/method/tyre/api/get_details": get_details,
        "/api/method/tyre.api.job_card": job_card,
        "/api/method/tyre.api.get_size":get_size,
        "/api/method/tyre.api.get_pattern":get_pattern,
        "/api/method/tyre.api.get_type":get_type,
        "/api/method/tyre.api.get_ItemCode":get_ItemCode,
        "/api/method/tyre.api.delete_vehicle":delete_vehicle,
        "/api/method/tyre.api.exist_mobile_number":exist_mobile_number,
        "/api/method/tyre.api.send_quotation":send_quotation
    }
}