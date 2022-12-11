frappe.pages['profile-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Your Profile',
		single_column: true
	});
	let nameValue = frappe.session.user_fullname
	let field = page.add_field({
		label: nameValue,
		fieldtype: 'Data',
		fieldname: 'full_name',
		read_only: 1,
		change() {
			console.log(field.get_value());
		}
	});
	let values = frappe.db.get_list('Gym Member', {
		fields: ['membership_type'],
		filters: {
			full_name: frappe.session.user_fullname
		}
	}).then(r => {
		let membership = r[0].membership_type
		let field = page.add_field({
			label: membership,
			fieldtype: 'Data',
			fieldname: 'membership_type',
			read_only: 1,
			change() {
				console.log(field.get_value());
			}
		});
	})
}


