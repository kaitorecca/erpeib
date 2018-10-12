// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Call Report', {
	refresh: function(frm) {

	},

	onload: function() {

		cur_frm.set_value("meeting_time", frappe.datetime.now_datetime());

	}
});
