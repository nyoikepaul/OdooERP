from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)

class MpesaController(http.Controller):

    @http.route('/payment/mpesa/callback', type='json', auth='public', methods=['POST'], csrf=False)
    def mpesa_callback(self, **kw):
        """Safaricom Daraja STK Push callback endpoint."""
        try:
            data = json.loads(request.httprequest.data)
            _logger.info("M-Pesa callback received: %s", data)

            stk = data.get('Body', {}).get('stkCallback', {})
            result_code = stk.get('ResultCode')
            checkout_id = stk.get('CheckoutRequestID')
            merchant_id = stk.get('MerchantRequestID')

            if result_code == 0:
                # Payment successful - extract metadata
                items = {
                    i['Name']: i.get('Value')
                    for i in stk.get('CallbackMetadata', {}).get('Item', [])
                }
                amount = items.get('Amount')
                mpesa_code = items.get('MpesaReceiptNumber')
                phone = items.get('PhoneNumber')
                _logger.info(
                    "M-Pesa payment SUCCESS | Code: %s | Amount: %s | Phone: %s",
                    mpesa_code, amount, phone
                )
                # TODO: reconcile against Odoo payment transaction by checkout_id
            else:
                _logger.warning(
                    "M-Pesa STK failed | CheckoutID: %s | ResultCode: %s | Desc: %s",
                    checkout_id, result_code, stk.get('ResultDesc')
                )
        except Exception as e:
            _logger.error("M-Pesa callback error: %s", str(e))

        return {"ResultCode": 0, "ResultDesc": "Accepted"}
