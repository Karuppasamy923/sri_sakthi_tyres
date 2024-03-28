// Copyright (c) 2024, krishna@aerele.in and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tyre Job Card", {
	// 	refresh(frm) {
	// 	},
	onload_post_render: function (frm) {
		frm.doc.service_advisor = frappe.session.user;
		frm.refresh_field("service_advisor");
	},
	after_save: function (frm) {
		frappe.call({
			method: "tyre.api.store_vehicle_details",
			args: {
				data: frm.doc,
			},
			// 	callback: function (res) {
			// 		console.log(res.message);
			// 	},
		});
	},
	// vehicle_no: function (frm) {
	// 	frappe.call({
	// 		method: "tyre.tyre.doctype.tyre_job_card.tyre_job_card.fetch_details",
	// 		args: {
	// 			doc: frm.doc,
	// 		},
	// 		callback: function (res) {
	// 			if (res.message["vehicle_no"]) {
	// 				let owner = res.message["customer"];
	// 				frm.set_value("customer", owner);
	// 			} else {
	// 				frm.set_value("customer", "");
	// 			}
	// 			// if (res.message["vehicle_no"]) {
	// 			// 	let driver = res.message["driver1"];
	// 			// 	frm.set_value("driver1", driver);
	// 			// } else {
	// 			// 	frm.set_value("driver1", "");
	// 			// }
	// 		},
	// 	});
	// },

	mail: function (frm) {
		debugger;
		if (frm.doc.mail && frm.doc.email == undefined) {
			frappe.msgprint({
				title: __("Notify"),
				indicator: "orange",
				message: __("Email Id is missing"),
			});
		}
	},
});
