{
    'name': 'Training Library',
    'version': '1.0',
    'summary': 'Module Training Odoo Library',
    'sequence': 10,
    'description': """Module Training Odoo Library""",
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/demo.xml',
        'views/library_views.xml',
        'views/book_model_views.xml',
        'views/rental_model_views.xml',
        'views/tr_library_menu.xml'
    ],
    'installable': True,
    'application': True
}
