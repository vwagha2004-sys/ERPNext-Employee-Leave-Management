import frappe
from frappe.model.document import Document

class LeaveRequest(Document):
    def validate(self):
        # Logic: Agar 'To Date' pehle ki hai, toh error dikhao
        if self.from_date and self.to_date:
            if self.to_date < self.from_date:
                frappe.throw("Galti: 'To Date', 'From Date' se pehle nahi ho sakti!")