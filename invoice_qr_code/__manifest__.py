{
    'name': 'Invoice Qr Code',
    'summary': 'Invoice Qr Code',
    'author': "Amr Othman",
    'company': '',
    'website': "",
    'version': '17.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'l10n_sa',
        'account',
    ],
    'data': [
        'reports/invoice_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

