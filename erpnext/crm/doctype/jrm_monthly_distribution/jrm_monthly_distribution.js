// Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('JRM Monthly Distribution', {
	refresh: function(frm) {

	}
});



cur_frm.cscript.onload = function(doc,cdt,cdn){
	if(doc.__islocal){
		var callback1 = function(r,rt){
			refresh_field('percentages');
		}

		return $c('runserverobj', {'method':'get_months', 'docs':doc}, callback1);
	}
}

cur_frm.cscript.refresh = function(doc,cdt,cdn){
	cur_frm.toggle_display('distribution_id', doc.__islocal);
}
