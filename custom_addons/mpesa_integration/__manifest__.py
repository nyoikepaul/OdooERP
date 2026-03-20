{
    'name': 'MPESA_INTEGRATION',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'High-security API kernel for Kenyan payment gateways.',
    'author': 'Paul Nyoike',
    'depends': ['base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
