# Copyright (c) 2026, renish and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document


class LibraryMember(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		email: DF.Data | None
		fname: DF.Data
		full_name: DF.Data | None
		lname: DF.Data | None
		phone: DF.Data | None
	# end: auto-generated types

	def before_save(self):
		self.full_name = f'{self.fname} {self.lname or ""}'
	
	def validate(self):
		if self.email:
			existing = frappe.db.exists("Library Member", {"email": self.email, "name": ("!=", self.name)})
			if existing:
				frappe.throw("A member with this email already exists.")