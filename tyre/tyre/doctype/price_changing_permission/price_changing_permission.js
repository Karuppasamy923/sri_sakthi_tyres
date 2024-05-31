// // Copyright (c) 2024, krishna@aerele.in and contributors
// // For license information, please see license.txt

// frappe.ui.form.on("Price changing permission", {
// 	after_save(frm) {
//         frappe.call({
//             method: "tyre.api.get_permission",
//             callback: function(response) {
//                 if (response.message) {
//                     frappe.msgprint(__('Permission updated successfully.'));
//                 } else {
//                     frappe.msgprint(__('Failed to update permission.'));
//                 }
//             },
//             error: function(error) {
//                 frappe.msgprint(__('An error occurred while updating permission.'));
//                 console.error(error);
//             }
//         });
// 	},
// });
