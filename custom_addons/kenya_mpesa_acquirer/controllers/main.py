from odoo import http
from odoo.http import request
import json

class MpesaController(http.Controller):
    @http.route('/payment/mpesa/callback', type='json', auth='public', methods=['POST'], csrf=False)
    def callback(self, **kw):
        data = json.loads(request.httprequest.data)
        return {"ResultCode": 0, "ResultDesc": "Success"}

    @http.route('/payment/mpesa/stk_push', type='json', auth='user')
    def stk_push(self, **kw):
        return {"status": "STK sent - check phone"}
