frappe.listview_settings['Transaction Management'] = {
	onload: function(me) {
		// frappe.route_options = {
		// 	"owner": frappe.session.user,
		// 	"status": "Open"
		// };
		me.page.set_title(__("Transaction Management"));

	},
	// hide_name_column: true,
	refresh: function(me) {
		// override assigned to me by owner
		 if (me.transaction_management_sidebar_setup) return;


		// add assigned by me
		me.page.add_sidebar_item(__("All Transaction"), function() {
			cur_list.filter_list.clear_filters()
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("Closing Next Month"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_area.add([[me.doctype, "execution", '<=', frappe.datetime.add_months(frappe.datetime.month_end(),1)]]);
			me.filter_area.add([[me.doctype, "execution", '>=', frappe.datetime.add_months(frappe.datetime.month_start(),1)]]);
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("Closing This Month"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_area.add([[me.doctype, "execution", '<=', frappe.datetime.month_end()]]);
			me.filter_area.add([[me.doctype, "execution", '>=', frappe.datetime.month_start()]]);			
		}, ".assigned-to-me");		

		me.page.add_sidebar_item(__("My Transaction"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_area.add([[me.doctype, "owner", '=', frappe.session.user]]);
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("New in last 7 days"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_area.add([[me.doctype, "created_on", '>=', frappe.datetime.add_days(frappe.datetime.get_today(),-7)]]);
		}, ".assigned-to-me");


		me.page.add_sidebar_item(__("Won"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_area.add([[me.doctype, "opportunity_status", '=', "FN-Hoàn thành, đã giải ngân"]]);
		}, ".assigned-to-me");		

		me.transaction_management_sidebar_setup = true;
	},

}