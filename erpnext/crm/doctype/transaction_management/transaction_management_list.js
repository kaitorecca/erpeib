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
			cur_list.filter_list.clear_filters();
			me.run();
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("Closing Next Month"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "execution", '<=', frappe.datetime.add_months(frappe.datetime.month_end(),1));
			me.filter_list.add_filter(me.doctype, "execution", '>=', frappe.datetime.add_months(frappe.datetime.month_start(),1));
			me.run();
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("Closing This Month"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_list.add_filter(me.doctype, "execution", '<=', frappe.datetime.month_end());
			me.filter_list.add_filter(me.doctype, "execution", '>=', frappe.datetime.month_start());
			me.run();			
		}, ".assigned-to-me");		

		me.page.add_sidebar_item(__("My Transaction"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "owner", '=', frappe.session.user);
			me.run();
		}, ".assigned-to-me");

		me.page.add_sidebar_item(__("New in last 7 days"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "creation", '>=', frappe.datetime.add_days(frappe.datetime.get_today(),-7));
			me.run();
		}, ".assigned-to-me");


		me.page.add_sidebar_item(__("Won"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "opportunity_status", '=', "FN-Hoàn thành, đã giải ngân");
			me.run();
		}, ".assigned-to-me");		

		me.transaction_management_sidebar_setup = true;
	},

}