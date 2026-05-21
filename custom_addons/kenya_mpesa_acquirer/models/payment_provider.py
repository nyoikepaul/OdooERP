from odoo import models, fields, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('mpesa', 'M-Pesa Kenya')],
        ondelete={'mpesa': 'set default'}
    )
    mpesa_consumer_key    = fields.Char("Consumer Key (Daraja)")
    mpesa_consumer_secret = fields.Char("Consumer Secret")
    mpesa_shortcode       = fields.Char("Business Shortcode")
    mpesa_passkey         = fields.Char("Lipa Na M-Pesa Passkey")
    mpesa_callback_url    = fields.Char("Callback URL", default="/payment/mpesa/callback")
    mpesa_sandbox         = fields.Boolean("Use Sandbox", default=True)

    def _mpesa_get_token(self):
        self.ensure_one()
        if self.code != 'mpesa':
            raise UserError(_("Provider is not M-Pesa"))
        mixin = self.env['mpesa.api.mixin']
        return mixin._get_access_token(
            self.mpesa_consumer_key,
            self.mpesa_consumer_secret,
            sandbox=self.mpesa_sandbox,
        )

    def action_test_mpesa_connection(self):
        """Button to test Daraja credentials from the provider form."""
        self.ensure_one()
        try:
            token = self._mpesa_get_token()
            if token:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('M-Pesa Connected'),
                        'message': _('Daraja credentials are valid ✅'),
                        'type': 'success',
                    }
                }
        except Exception as e:
            raise UserError(str(e)) from e
