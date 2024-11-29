{
    'name': 'SO PO Edits',
    'summary': 'SO PO Edits',
    'author': "Amr Othman",
    'company': '',
    'website': "",
    'version': '17.0',
    'category': 'Purchase',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'web',
        'l10n_sa',
        'account',
        'sale',
        'purchase'
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/stock_return_wizard.xml',
        'views/account_move.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml',
        'reports/invoice_report.xml',
        'reports/po_report.xml',
        'reports/so_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

