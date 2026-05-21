from odoo import models, fields, api
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class EstateLease(models.Model):
    _name = 'estate.lease'
    _description = 'Property Lease / Tenancy Agreement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_start desc'

    name = fields.Char("Lease Ref", readonly=True, copy=False, default='New')
    property_id = fields.Many2one('estate.property', string="Property",
                                  required=True, ondelete='restrict', tracking=True)
    tenant_id   = fields.Many2one('res.partner', string="Tenant",
                                  required=True, tracking=True)
    date_start  = fields.Date("Start Date", required=True)
    date_end    = fields.Date("End Date",   required=True)
    monthly_rent= fields.Monetary("Monthly Rent (KES)", currency_field='currency_id',
                                  related='property_id.monthly_rent', readonly=False)
    currency_id = fields.Many2one('res.currency', default=lambda s: s.env.ref('base.KES'))
    deposit     = fields.Monetary("Security Deposit (KES)", currency_field='currency_id')
    status      = fields.Selection([
        ('draft',    'Draft'),
        ('active',   'Active'),
        ('expired',  'Expired'),
        ('cancelled','Cancelled'),
    ], default='draft', tracking=True)
    payment_ids = fields.One2many('account.move', 'lease_id', string="Rent Invoices")
    payment_count = fields.Integer(compute='_compute_payment_count')
    notes       = fields.Text("Notes")

    @api.depends('payment_ids')
    def _compute_payment_count(self):
        for rec in self:
            rec.payment_count = len(rec.payment_ids)

    @api.constrains('date_start', 'date_end')
    def _check_dates(self):
        for rec in self:
            if rec.date_end <= rec.date_start:
                raise ValidationError("End date must be after start date.")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('estate.lease') or 'New'
        return super().create(vals_list)

    def action_activate(self):
        self.write({'status': 'active'})
        self.property_id.write({'status': 'leased'})

    def action_cancel(self):
        self.write({'status': 'cancelled'})
        self.property_id.write({'status': 'available'})

    def action_generate_rent_invoice(self):
        """Generate next month rent invoice for this lease."""
        self.ensure_one()
        invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.tenant_id.id,
            'lease_id': self.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [(0, 0, {
                'name': f'Rent - {self.property_id.name} ({fields.Date.today().strftime("%B %Y")})',
                'quantity': 1,
                'price_unit': self.monthly_rent,
            })]
        })
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': invoice.id,
            'view_mode': 'form',
        }
