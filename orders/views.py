from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import OrderForm
from cart.cart import Cart
from .models import OrderItem


def order_create_view(request):
    form = OrderForm()
    cart = Cart(request)
    if len(cart) == 0:
        messages.warning(request, "please add items to your cart!")
        return redirect("movie_list")
    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()

            for item in cart:
                order = form_obj
                product = item["movie_obj"]
                quantity = item["quantity"]
                quantity_total_price = quantity * product.price
                OrderItem.objects.create(order=order, product=product, quantity=quantity,
                                         quantity_total_price=quantity_total_price)
                messages.success(request, "your order has been saved")
            cart.clear()

    return render(request, "orders/order_create.html", context={"form": form})
