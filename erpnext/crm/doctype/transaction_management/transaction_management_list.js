frappe.listview_settings['Transaction Management'] = {
	onload: function(me) {
		// frappe.route_options = {
		// 	"owner": frappe.session.user,
		// 	"status": "Open"
		// };
		me.page.set_title(__("Transaction Management"));

	},

	add_extra_sidebar: function(me){
		var parent = me.sidebar.find(".sidebar-menu.standard-actions");
		var li = '<ul class="list-unstyled sidebar-menu sidebar-choose-view"><li class="divider"></li>  <li class="h6 stat-label">Choose your view</li></ul>';

		li.insertAfter(parent);
	},

	add_extra_sidebar_item: function(label, action, insert_after, prepend) {
		var parent = me.sidebar.find(".sidebar-menu.sidebar-choose-view");
		var li = $('<li>');
		var link = $('<a>').html(label).on("click", action).appendTo(li);

		if(insert_after) {
			li.insertAfter(parent.find(insert_after));
		} else {
			if(prepend) {
				li.prependTo(parent);
			} else {
				li.appendTo(parent);
			}
		}
		return link;
	},


	// hide_name_column: true,
	refresh: function(me) {
		// override assigned to me by owner
		 if (me.transaction_management_sidebar_setup) return;

		 this.add_sidebar_item();


		// add assigned by me
		this.add_extra_sidebar_item(__("All Transaction"), function() {
			cur_list.filter_list.clear_filters();
			me.run();
		}, ".stat-label");

		this.add_extra_sidebar_item(__("Closing Next Month"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "execution", '<=', frappe.datetime.add_months(frappe.datetime.month_end(),1));
			me.filter_list.add_filter(me.doctype, "execution", '>=', frappe.datetime.add_months(frappe.datetime.month_start(),1));
			me.run();
		}, ".stat-label");

		this.add_extra_sidebar_item(__("Closing This Month"), function() {
			cur_list.filter_list.clear_filters()
			me.filter_list.add_filter(me.doctype, "execution", '<=', frappe.datetime.month_end());
			me.filter_list.add_filter(me.doctype, "execution", '>=', frappe.datetime.month_start());
			me.run();			
		}, ".stat-label");		

		this.add_extra_sidebar_item(__("My Transaction"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "owner", '=', frappe.session.user);
			me.run();
		}, ".stat-label");

		this.add_extra_sidebar_item(__("New in last 7 days"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "creation", '>=', frappe.datetime.add_days(frappe.datetime.get_today(),-7));
			me.run();
		}, ".stat-label");


		this.add_extra_sidebar_item(__("Won"), function() {
			cur_list.filter_list.clear_filters();
			me.filter_list.add_filter(me.doctype, "opportunity_status", '=', "FN-Hoàn thành, đã giải ngân");
			me.run();
		}, ".stat-label");		

		me.transaction_management_sidebar_setup = true;
	},

}