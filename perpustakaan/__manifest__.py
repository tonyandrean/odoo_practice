# -*- coding: utf-8 -*-
{
    'name': "perpustakaan",

    'summary': "sisfor_perpustakaan",

    'description': "Module untuk sistem informasi Perpustakaan",

    'author': "semangkha",
    'website': "https://github.com/tonyandrean",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'images': ['static/description/icon.png'],

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/akun_perpus_view.xml',
        'views/daftar_buku_view.xml',
        'views/master_data_view.xml',
        'views/peminjaman_buku_view.xml',
        'views/menu.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
