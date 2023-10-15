from django.urls import path
from .views import payment_process_view, payment_process_view_sandbox, payment_callback_view_sandbox

app_name = "payment"

urlpatterns = [
    path("process/", payment_process_view_sandbox, name="payment_process"),
    path("callback/", payment_callback_view_sandbox, name="payment_callback"),
]
