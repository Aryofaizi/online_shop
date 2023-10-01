from django.urls import path

from .views import add_to_cart, cart_detail_view, remove_from_cart, clear_cart


urlpatterns = [
    path("", cart_detail_view, name="cart_detail"),
    path("add/<int:movie_id>/", add_to_cart, name="cart_add"),
    path("remove/<int:movie_id>/", remove_from_cart, name="cart_remove"),
    path("clear/", clear_cart, name="cart_clear"),
]
