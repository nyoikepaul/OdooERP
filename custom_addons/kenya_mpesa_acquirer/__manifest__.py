{
    'name': "Kenya M-Pesa Payment Acquirer",
    'version': '18.0.1.0.0',
    'category': 'Accounting/Payment Acquirers',
    'summary': 'M-Pesa STK Push, C2B, B2C, Webhooks - Full Daraja API for Kenya',
    'description': """<div style="text-align:center">
        <h2>✅ Production-ready M-Pesa for Odoo</h2>
        <p>STK Push • Automatic reconciliation • KRA eTIMS invoices • Works with Sales, POS, eCommerce</p>
    </div>""",
    'author': "Paul Nyoike - Nairobi",
    'website': "https://github.com/nyoikepaul",
    'depends': ['payment'],
    'data': [
        'security/ir.model.access.csv',
        'views/payment_provider_views.xml',
        'data/payment_method.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
