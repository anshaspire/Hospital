# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Mangement',
    'version' : '1.0.0',
    'sequence' : -150,
    'category': 'hospitals',
    'author' : 'odoo',
    'summary': 'hospitals are the best',
    'description': 'hospital management system is very important system',
    'demo' : [],
    'data' : [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/appointment_copy.xml',
        'views/appointment.xml',
        'views/res_config_settings_views.xml',
        'views/opration.xml',
        'wizards/cancel_wizard.xml',
        'wizards/emails.xml',
        'reoprt/report.xml'
    ],
    'depends' : ['mail','product'],
    'application' : True,
    'installabel' : True,
    'license' : 'LGPL-3'
}
