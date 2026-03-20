{
    'name': 'M-Pesa Connector Pro',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Localisation',
    'summary': 'Secure M-Pesa STK Push and C2B Kernel for Kenya.',
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
