{
    'name': 'M-Pesa Connector Core',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment',
    'summary': 'Core M-Pesa Daraja API kernel.',
    'author': 'Paul Nyoike - Nairobi',
    'website': 'https://github.com/Daniel815266/OdooERP',
    'depends': ['account', 'payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
