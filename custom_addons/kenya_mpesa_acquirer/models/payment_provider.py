from odoo import models, fields

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('mpesa', 'M-Pesa Kenya')], ondelete={'mpesa': 'set default'})
    mpesa_consumer_key = fields.Char("Consumer Key (Daraja)")
    mpesa_consumer_secret = fields.Char("Consumer Secret")
    mpesa_shortcode = fields.Char("Business Shortcode")
    mpesa_passkey = fields.Char("Lipa Na M-Pesa Passkey")
    mpesa_callback_url = fields.Char("Callback URL", default="/payment/mpesa/callback")
