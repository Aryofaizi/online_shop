from django.urls import path
from .views import payment_process_view

app_name = "payment"

urlpatterns = [
    path("process/", payment_process_view, name="payment_process"),
]
