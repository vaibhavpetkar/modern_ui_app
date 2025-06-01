# -*- coding: utf-8 -*-
app_name = "modern_ui_app"
app_title = "Modern UI App"
app_publisher = "Manus AI"
app_description = "Modern UI Theme for ERPNext"
app_email = "noreply@example.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/modern_ui_app/css/modern_ui_theme.css"
# app_include_js = "/assets/modern_ui_app/js/modern_ui_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/modern_ui_app/css/modern_ui_app.css"
# web_include_js = "/assets/modern_ui_app/js/modern_ui_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "modern_ui_app/public/scss/website"

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
# -----------
# include app icons in desk
# app_include_icons = "modern_ui_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# -----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "modern_ui_app.utils.jinja_methods",
#	"filters": "modern_ui_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "modern_ui_app.install.before_install"
# after_install = "modern_ui_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "modern_ui_app.uninstall.before_uninstall"
# after_uninstall = "modern_ui_app.uninstall.after_uninstall"

# Integration Setup
# -------------------
# To set up dependencies/integrations with other apps
# Name of the app being integrated is given as dictionary key
# an example is given below
# integrations = {
#	"frappe_integration_app": {
#		"app_installed": "modern_ui_app.integration.app_installed",
#		"app_uninstalled": "modern_ui_app.integration.app_uninstalled"
#	}
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "modern_ui_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "modern_ui_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#	when a supporting document is cancelled
# cancel_exempted_doctypes = ["User"]

# Ignore links to specified DocTypes when deleting documents
# ----------------------------------------------------------- -
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["modern_ui_app.utils.before_request"]
# after_request = ["modern_ui_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["modern_ui_app.utils.before_job"]
# after_job = ["modern_ui_app.utils.after_job"]

# User Data Protection
# ---------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"is_child_table": 1,
#		"ignore_on_export": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"is_child_table": 1,
#		"ignore_on_export": 1,
#	},
# ]

# Scheduled Tasks
# --------------- -

# scheduler_events = {
#	"all": [
#		"modern_ui_app.tasks.all"
#	],
#	"daily": [
#		"modern_ui_app.tasks.daily"
#	],
#	"hourly": [
#		"modern_ui_app.tasks.hourly"
#	],
#	"weekly": [
#		"modern_ui_app.tasks.weekly"
#	],
#	"monthly": [
#		"modern_ui_app.tasks.monthly"
#	],
# }

# Testing
# ------- -

# before_tests = "modern_ui_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "modern_ui_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "modern_ui_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#	when a supporting document is cancelled
# cancel_exempted_doctypes = ["User"]

# Ignore links to specified DocTypes when deleting documents
# ----------------------------------------------------------- -
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["modern_ui_app.utils.before_request"]
# after_request = ["modern_ui_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["modern_ui_app.utils.before_job"]
# after_job = ["modern_ui_app.utils.after_job"]

# User Data Protection
# ---------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"is_child_table": 1,
#		"ignore_on_export": 1,
#	},
#	{
#		"doctype": "{doctype_name}",
#		"filter_by": "{filter_by}",
#		"is_child_table": 1,
#		"ignore_on_export": 1,
#	},
# ]

# Scheduled Tasks
# --------------- -

# scheduler_events = {
#	"all": [
#		"modern_ui_app.tasks.all"
#	],
#	"daily": [
#		"modern_ui_app.tasks.daily"
#	],
#	"hourly": [
#		"modern_ui_app.tasks.hourly"
#	],
#	"weekly": [
#		"modern_ui_app.tasks.weekly"
#	],
#	"monthly": [
#		"modern_ui_app.tasks.monthly"
#	],
# }

# Testing
# ------- -

# before_tests = "modern_ui_app.install.before_tests"

