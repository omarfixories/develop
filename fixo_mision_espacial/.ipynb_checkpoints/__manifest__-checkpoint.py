# -*- coding: utf-8 -*-
{
    'name': "Mision Espacial",

    'summary': """ Sistema de logistica para la mision espacial del odoo """,

    'description': """
         Sistema de logistica para la mision espacial del odoo
         -Administración de la nave espacial
         -Administración de la tripulación
    """,

    'author': "Fixories",
    'website': "http://www.Fixories.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
