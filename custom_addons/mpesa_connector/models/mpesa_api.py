import base64, logging, requests
from datetime import datetime
from odoo import models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)
DARAJA_SANDBOX = "https://sandbox.safaricom.co.ke"
DARAJA_LIVE    = "https://api.safaricom.co.ke"

class MpesaAPIMixin(models.AbstractModel):
    _name = "mpesa.api.mixin"
    _description = "M-Pesa Daraja API Mixin"

    def _daraja_url(self, sandbox=False):
        return DARAJA_SANDBOX if sandbox else DARAJA_LIVE

    def _get_access_token(self, consumer_key, consumer_secret, sandbox=False):
        creds = base64.b64encode(f"{consumer_key}:{consumer_secret}".encode()).decode()
        try:
            r = requests.get(
                f"{self._daraja_url(sandbox)}/oauth/v1/generate?grant_type=client_credentials",
                headers={"Authorization": f"Basic {creds}"}, timeout=10)
            r.raise_for_status()
            return r.json().get("access_token")
        except requests.RequestException as e:
            raise UserError(f"M-Pesa auth failed: {e}") from e

    def _stk_push(self, token, shortcode, passkey, phone,
                  amount, callback_url, account_ref, sandbox=False):
        ts  = datetime.now().strftime("%Y%m%d%H%M%S")
        pwd = base64.b64encode(f"{shortcode}{passkey}{ts}".encode()).decode()
        payload = {
            "BusinessShortCode": shortcode, "Password": pwd, "Timestamp": ts,
            "TransactionType": "CustomerPayBillOnline", "Amount": int(amount),
            "PartyA": phone, "PartyB": shortcode, "PhoneNumber": phone,
            "CallBackURL": callback_url, "AccountReference": account_ref,
            "TransactionDesc": f"Payment {account_ref}",
        }
        try:
            r = requests.post(
                f"{self._daraja_url(sandbox)}/mpesa/stkpush/v1/processrequest",
                json=payload, headers={"Authorization": f"Bearer {token}"}, timeout=15)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            raise UserError(f"STK Push failed: {e}") from e
