{
    'name': 'M-Pesa Connector Core',
    'version': '1.0',
    'category': 'Accounting',
    'author': 'Paul Nyoike',
    'depends': ['account', 'payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
