# Copyright (c) 2026, renish and contributors
# For license information, please see license.txt

# import frappe
from genericpath import exists

import frappe
from frappe.model.docstatus import DocStatus
from frappe.model.document import Document


class LibraryMembership(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		from_date: DF.Date | None
		full_name: DF.Data | None
		library_member: DF.Link
		paid: DF.Check
		to_date: DF.Date | None
	# end: auto-generated types

	
	def before_submit(self):
		exists = frappe.db.exists(
			"Library Membership",
			{
				"library_member": self.library_member,
				"docstatus": DocStatus.submitted(),
				# check if the membership's end date is later than this membership's start date
				"to_date": (">", self.from_date),
			},
		)
		if exists:
			frappe.throw("There is an active membership for this member")
