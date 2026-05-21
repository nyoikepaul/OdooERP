from odoo.tests.common import HttpCase
import json

class TestMpesaCallback(HttpCase):
    def test_callback_success(self):
        payload = {
            "Body": {
                "stkCallback": {
                    "ResultCode": 0,
                    "CheckoutRequestID": "ws_CO_TEST123",
                    "MerchantRequestID": "MR_TEST456",
                    "ResultDesc": "The service request is processed successfully.",
                    "CallbackMetadata": {
                        "Item": [
                            {"Name": "Amount", "Value": 1500},
                            {"Name": "MpesaReceiptNumber", "Value": "RGQ12TEST"},
                            {"Name": "PhoneNumber", "Value": 254712345678},
                        ]
                    }
                }
            }
        }
        resp = self.url_open(
            '/payment/mpesa/callback',
            data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        self.assertEqual(resp.status_code, 200)
