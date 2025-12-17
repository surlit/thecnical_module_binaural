# -*- coding: utf-8 -*-
{
    'name': "Thecnical Module",

    'summary': "Thecnical Module",

    'description': """
Long description of module's purpose
    """,
    'application':True,
    'sequence':1,
    'author': "Luis Silva",
    'website': "https://www.luissilva.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/tipo_cliente_data.xml',
        'views/views_res_partner_custom.xml',
        'views/res_config_cus_view.xml',
        'views/tipo_cliente_view.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

