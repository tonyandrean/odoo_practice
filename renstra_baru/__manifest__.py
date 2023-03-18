# -*- coding: utf-8 -*-
{
    'name': "renstra_ft",

    'summary': "renstra_ft_udinus",

    'description': "Module For inputing data renstra ft udinus",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','board'],

    # always loaded
    'data': [
        'security/secur.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/koordinator_view.xml',
        'views/akreditasi_view.xml',
        'views/survey.xml',
        'views/survey_tenaga_pendidik.xml',
        'data/sequence_id.xml',
        'views/akreditasi_dashboard.xml',
        # 'views/kelulusan_view.xml',
        # 'views/kelulusan_dashboard.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
