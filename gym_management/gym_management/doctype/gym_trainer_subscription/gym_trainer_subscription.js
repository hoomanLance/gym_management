// Copyright (c) 2022, Lance and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Trainer Subscription', {
	refresh(frm) {
	    console.log("user full name is: ", frappe.session.user_fullname);
		if(frm.doc.__islocal) {
		    frm.set_value('full_name', frappe.session.user_fullname);
		    frm.refresh_field('full_name')
		}
	}
})
