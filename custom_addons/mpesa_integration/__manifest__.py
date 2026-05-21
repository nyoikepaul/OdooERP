{
    'name': 'M-Pesa Integration',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment',
    'summary': 'High-security API kernel for Kenyan payment gateways.',
    'author': 'Paul Nyoike - Nairobi',
    'website': 'https://github.com/NyoikePaul/OdooERP',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
