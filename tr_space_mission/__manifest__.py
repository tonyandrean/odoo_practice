{
    'name': 'Training Space Mission',
    'version': '1.0',
    'summary': 'Module Training Odoo Space Mission',
    'sequence': 10,
    'description': """Module Training Odoo Mission""",
    'depends': ['base', 'project'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/demo.xml',
        'wizard/project_wizard.xml',
        'views/spaceship_views.xml',
        'views/mission_model_views.xml',
        'views/project_views.xml',
        'views/space_mission_menu.xml'
    ],
    'installable': True,
    'application': True
}
