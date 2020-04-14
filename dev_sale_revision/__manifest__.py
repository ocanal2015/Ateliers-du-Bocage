# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Sale Revision Number & History',
    'version': '13.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Sales Management',
    'description':
        """
 odoo Module add below functionality into odoo

        1.Create Revision order for the sale order\n
        
        Sale Revision
        Odoo sale revision 
        Odoo sale revision history 
        odoo revision history 
        

    """,
    'summary': 'Odoo app will help to add Sale Revision order of sale order',
    'depends': [
        'sale_management'
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    
    # author and support Details =============#
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',    
    'maintainer': 'DevIntelle Consulting Service Pvt.Ltd', 
    'support': 'devintelle@gmail.com',
    'price':15.0,
    'currency':'EUR',
    #'live_test_url':'https://youtu.be/A5kEBboAh_k',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
