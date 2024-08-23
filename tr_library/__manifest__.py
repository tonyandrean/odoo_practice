{
    'name': 'Training Library',
    'version': '1.0',
    'summary': 'Module Training Odoo Library',
    'sequence': 10,
    'description': """Module Training Odoo Library""",
    'depends': ['base', 'project'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/demo.xml',
        'data/ir_sequence.xml',
        'wizard/book_wizard.xml',
        'views/library_views.xml',
        'views/book_model_views.xml',
        'views/rental_model_views.xml',
        'views/project_views.xml',
        'views/tr_library_menu.xml'
    ],
    'installable': True,
    'application': True
}
