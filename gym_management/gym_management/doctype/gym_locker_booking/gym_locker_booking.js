// Copyright (c) 2022, Lance and contributors
// For license information, please see license.txt

frappe.ui.form.on('Gym Locker Booking', {
	refresh(frm) {
	    frm.fields_dict['locker_number'].get_query = function(doc) {
	        return {
	            filters: {
	                "is_booked": "No"
	            }
	        }
	    }
		if(frm.doc.__islocal) {
		    frm.set_value('full_name', frappe.session.user_fullname);
		    frm.refresh_field('full_name')
		}
	}
});
frappe.ui.form.on('Gym Locker Booking', {
    before_save: function(frm, cdt, cdn) {
        console.log("Before Save");
        frappe.db.set_value('Gym Locker', frm.doc.locker_number, 'is_booked', 'Yes');
        console.log("changed is_booked to yes for: ", frm.doc.locker_number);
    }
});
