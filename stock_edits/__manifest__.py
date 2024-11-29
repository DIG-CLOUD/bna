{
    'name': 'Stock Edits',
    'summary': 'Stock Edits',
    'author': "Amr Othman",
    'company': '',
    'website': "",
    'version': '17.0',
    'category': 'Inventory',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'stock',
        'sale_stock',
        'purchase_stock'
    ],
    'data': [
        'views/stock_move_line.xml',
        'views/stock_warehouse.xml',
        'views/sale_order.xml',
        'views/account_move.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

