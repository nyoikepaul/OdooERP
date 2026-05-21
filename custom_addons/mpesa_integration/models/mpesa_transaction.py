from odoo import models, fields

class MpesaTransaction(models.Model):
    _name = 'mpesa.transaction'
    _description = 'M-Pesa Transaction Log'
    _order = 'create_date desc'
    _rec_name = 'receipt_number'

    receipt_number  = fields.Char("M-Pesa Receipt", readonly=True, index=True)
    phone           = fields.Char("Phone Number")
    amount          = fields.Float("Amount (KES)")
    checkout_id     = fields.Char("Checkout Request ID", readonly=True)
    merchant_id     = fields.Char("Merchant Request ID", readonly=True)
    result_code     = fields.Integer("Result Code")
    result_desc     = fields.Char("Result Description")
    status          = fields.Selection([
        ('pending',  'Pending'),
        ('success',  'Success'),
        ('failed',   'Failed'),
        ('cancelled','Cancelled'),
    ], default='pending', index=True)
    invoice_id      = fields.Many2one('account.move', string="Invoice", ondelete='set null')
    raw_payload     = fields.Text("Raw Callback Payload")
    create_date     = fields.Datetime("Received At", readonly=True)

    def name_get(self):
        return [(r.id, r.receipt_number or f'TXN-{r.id}') for r in self]
