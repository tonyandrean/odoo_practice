{
    'name': 'Sequence Invoice',
    'version': '1.0',
    'summary': 'Sequence for invoices, bills, and journal entries',
    'sequence': 10,
    'description': """""",
    'author': 'tonigiri',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_branch_view.xml',
        'views/res_users_view.xml',
        'views/menu_res_branch.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
