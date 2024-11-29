{
    'name': 'HR Edits',
    'summary': 'HR Edits',
    'author': "Amr Othman",
    'company': '',
    'website': "",
    'version': '17.0',
    'category': 'Hr',
    'license': 'AGPL-3',
    'sequence': 1,
    'depends': [
        'base',
        'hr_contract'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee.xml',
        'views/hr_contract.xml',
        'views/employee_branch.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

