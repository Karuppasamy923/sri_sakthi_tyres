// Copyright (c) 2024, krishna@aerele.in and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle Details", {
	// 	refresh(frm) {
	// 	},
	before_save: function (frm) {
		frm.doc.license_plate = frm.doc.license_plate.toUpperCase().replace(/\s+/g, "");
		frm.refresh_field("license_plate");
	},
});
