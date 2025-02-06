{
    'name': "Stock Picking Label",
    'version': '1.0.0',
    'summary': """Print label Stock Picking with Barcode and QR Code""",
    'category': 'Inventory',
    'author': 'tonigiri',
    'depends': ['base', 'stock'],
    'data': [
        'data/paperformat.xml',
        'report/action_stock_picking_label.xml',
        'report/report_stock_picking_label.xml',
    ],
    'license': "OPL-1",
    'installable': True,
    'application': False,
}
