# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
	'name': "Custom CRM Sale Order Module",
	'version': "16.0.0.1",
	'category': "CRM",
	'summary': "This module is used for the purpose of customise sale order form as per the crm service customization *",
	'description':	"""
					Modify the sale order line header
					Append crm related field in the model
					Make Report of the the crm related sale order invoice and print view
					""",
	'author': "Kolpolok",
	'license': 'OPL-1',
	"website" : "http://kolpoloktechnologies.com",
	"price": 00,
	"currency": 'BDT',
	'depends': ['base','sale','project'],
	'data': [
				'security/ir.model.access.csv',
				# 'wizard/import_employee_view.xml',
				'views/custom_inherit_sale_order.xml',
				'views/custom_inherit_project_task.xml',
				'report/custom_sale_quotation_print_view.xml',
				# 'report/custom_sale_report_order_templates.xml',
			],
	'demo': [],
	'qweb': [],
	'installable': True,
	'auto_install': False,
	'application': False,
	# "live_test_url":'https://youtu.be/oqlqPMfwWo0',
	# "images":['static/description/Banner.gif'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
