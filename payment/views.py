from django.shortcuts import render, get_object_or_404
from orders.models import Order
import requests
import json
from config import settings


def payment_process_view(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    rial_total_order_price = order.get_toman_total_price() * 10
    zarinpal_url = 'https://api.zarinpal.com/pg/v4/payment/request.json'
    data = {
        'merchant_id': settings.MERCHANT_ID,
        'amount': rial_total_order_price,
        'description':
            f'id={order.id},'
            f'name={request.user.first_name},'
            f'lastname={request.user.last_name}',
        'callback_url': '127.0.0.1:8000',
    }
    request_header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(zarinpal_url, data=json.dumps(data), headers=request_header)
