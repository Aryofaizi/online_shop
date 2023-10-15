from django.shortcuts import render, get_object_or_404, redirect, reverse
from orders.models import Order
import requests
import json
from config import settings
from django.http import HttpResponse
from django.utils.translation import gettext as _


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
    data = response.json()["data"]
    authority = data["authority"]
    order.zarinpal_authority = authority
    order.save()
    if 'errors' not in data or len(data["errors"]) == 0:
        return redirect(f"https://www.zarinpal.com/pg/StartPay/{authority}")
    else:
        return HttpResponse("payment unsuccessful")


def payment_process_view_sandbox(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    rial_total_order_price = order.get_toman_total_price() * 10
    zarinpal_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json'
    data = {
        'MerchantID': 'abcdefabcdefabcdefabcdefabcdefabcdef',
        'Amount': rial_total_order_price,
        'Description':
            f'''id={order.id},
            name={request.user.first_name},
            lastname={request.user.last_name}''',
        'CallbackURL':request.build_absolute_uri(reverse("payment:payment_callback")),
    }
    request_header = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    response = requests.post(zarinpal_url, data=json.dumps(data), headers=request_header)
    data = response.json()
    print(data)
    authority = data["Authority"]
    order.zarinpal_authority = authority
    order.save()
    if 'errors' not in data or len(data["errors"]) == 0:
        return redirect(f"https://sandbox.zarinpal.com/pg/StartPay/{authority}")
    else:
        return HttpResponse("payment unsuccessful")


def payment_callback_view_sandbox(request):
    authority = request.GET.get("Authority")
    status = request.GET.get("Status")
    order = get_object_or_404(Order, zarinpal_authority=authority)
    rial_total_order_price = order.get_toman_total_price() * 10
    request_headers = {"Content": "application/json", "accept": "application/json"}
    data = {
        "MerchantID": 'abcdefabcdefabcdefabcdefabcdefabcdef',
        'Amount': rial_total_order_price,
        'Authority': authority,
    }
    verify_url = 'https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json'
    response = requests.post(url=verify_url, data=json.dumps(data), headers=request_headers)
    data = response.json()
    print(data)
    if len(data["errors"]) == 0:
        payment_code = 100
        if status == "OK":
            if payment_code == 100:
                order.is_paid = True
                order.zarinpal_ref_id = 201
                order.zarinpal_data = data
                order.save()
                return HttpResponse(_('successful payment '))
            elif payment_code == 101:
                return HttpResponse(_("successful payment but has been verified once"))
            else:
                return HttpResponse(_("unsuccessful payment "))
        else:
            return HttpResponse(_("unsuccessful payment "))
    else:
        return HttpResponse(_("unsuccessful payment "))


