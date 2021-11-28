# Copyright (c) 2021, tyler and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
#import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.naming import getseries
from frappe.model.document import Document

class GadgetProduct(WebsiteGenerator):
        # pass
        def autoname(self):
        # select a project name based on customer
                prefix = 'P-{}-'.format(self.product_name)
                self.product_id = getseries(prefix, 3)

