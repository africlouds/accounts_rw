# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "accounts_rw"
app_title = "Accounts RW"
app_publisher = "Africlouds Ltd"
app_description = "Accounts Customization for Rwanda"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "arwema@gmail.com"
app_license = "MIT"
fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/accounts_rw/css/accounts_rw.css"
# app_include_js = "/assets/accounts_rw/js/accounts_rw.js"

# include js, css files in header of web template
# web_include_css = "/assets/accounts_rw/css/accounts_rw.css"
# web_include_js = "/assets/accounts_rw/js/accounts_rw.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "accounts_rw.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "accounts_rw.install.before_install"
# after_install = "accounts_rw.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "accounts_rw.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"accounts_rw.tasks.all"
# 	],
# 	"daily": [
# 		"accounts_rw.tasks.daily"
# 	],
# 	"hourly": [
# 		"accounts_rw.tasks.hourly"
# 	],
# 	"weekly": [
# 		"accounts_rw.tasks.weekly"
# 	]
# 	"monthly": [
# 		"accounts_rw.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "accounts_rw.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "accounts_rw.event.get_events"
# }

