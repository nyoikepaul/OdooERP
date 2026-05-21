from odoo import http
from odoo.http import request
import json
import logging

_logger = logging.getLogger(__name__)


class MpesaController(http.Controller):

    @http.route('/payment/mpesa/callback', type='json', auth='public', methods=['POST'], csrf=False)
    def mpesa_callback(self, **kw):
        """Safaricom Daraja STK Push callback — saves to mpesa.transaction log."""
        try:
            raw = request.httprequest.data
            data = json.loads(raw)
            _logger.info("M-Pesa callback received: %s", data)

            stk = data.get('Body', {}).get('stkCallback', {})
            result_code = stk.get('ResultCode')
            checkout_id = stk.get('CheckoutRequestID', '')
            merchant_id = stk.get('MerchantRequestID', '')
            result_desc = stk.get('ResultDesc', '')

            tx_vals = {
                'checkout_id': checkout_id,
                'merchant_id': merchant_id,
                'result_code': result_code,
                'result_desc': result_desc,
                'raw_payload': raw.decode('utf-8'),
                'status':      'success' if result_code == 0 else 'failed',
            }

            if result_code == 0:
                items = {
                    i['Name']: i.get('Value')
                    for i in stk.get('CallbackMetadata', {}).get('Item', [])
                }
                tx_vals.update({
                    'receipt_number': items.get('MpesaReceiptNumber'),
                    'amount':         float(items.get('Amount', 0)),
                    'phone':          str(items.get('PhoneNumber', '')),
                })
                _logger.info(
                    "M-Pesa SUCCESS | Receipt: %s | Amount: %s | Phone: %s",
                    tx_vals['receipt_number'], tx_vals['amount'], tx_vals['phone']
                )
            else:
                _logger.warning(
                    "M-Pesa FAILED | CheckoutID: %s | Code: %s | Desc: %s",
                    checkout_id, result_code, result_desc
                )

            # Save to transaction log
            request.env['mpesa.transaction'].sudo().create(tx_vals)

            # Reconcile against pending payment transaction if exists
            if result_code == 0 and checkout_id:
                payment_tx = request.env['payment.transaction'].sudo().search(
                    [('acquirer_reference', '=', checkout_id)], limit=1
                )
                if payment_tx:
                    payment_tx.sudo()._set_done()
                    _logger.info("Payment transaction %s marked as done", payment_tx.reference)

        except Exception as e:
            _logger.exception("M-Pesa callback processing error: %s", str(e))

        # Always return success to Safaricom — never let them retry
        return {"ResultCode": 0, "ResultDesc": "Accepted"}

    @http.route('/payment/mpesa/stk_push', type='json', auth='user', methods=['POST'])
    def stk_push(self, amount, phone, account_ref, **kw):
        """Initiate STK Push from frontend/POS."""
        provider = request.env['payment.provider'].sudo().search(
            [('code', '=', 'mpesa'), ('state', '!=', 'disabled')], limit=1
        )
        if not provider:
            return {'error': 'M-Pesa provider not configured'}

        try:
            token = provider._mpesa_get_token()
            mixin = request.env['mpesa.api.mixin']
            result = mixin._stk_push(
                token=token,
                shortcode=provider.mpesa_shortcode,
                passkey=provider.mpesa_passkey,
                phone=phone,
                amount=amount,
                callback_url=request.httprequest.host_url.rstrip('/') + '/payment/mpesa/callback',
                account_ref=account_ref,
                sandbox=provider.mpesa_sandbox,
            )
            # Log pending transaction
            request.env['mpesa.transaction'].sudo().create({
                'checkout_id': result.get('CheckoutRequestID'),
                'merchant_id': result.get('MerchantRequestID'),
                'phone':       phone,
                'amount':      amount,
                'status':      'pending',
            })
            return {'success': True, 'checkout_id': result.get('CheckoutRequestID')}
        except Exception as e:
            _logger.error("STK Push error: %s", str(e))
            return {'error': str(e)}
