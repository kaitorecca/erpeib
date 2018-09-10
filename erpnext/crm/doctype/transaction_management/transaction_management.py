# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from erpnext.accounts.party import validate_party_accounts, get_dashboard_info, get_timeline_data

class TransactionManagement(Document):
	def onload(self):
		"""Load address and contacts in `__onload`"""
		self.load_dashboard_info()