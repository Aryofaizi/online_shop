from django.shortcuts import render, get_object_or_404, redirect
from movies.models import Movie
from cart.cart import Cart
from cart.forms import CartForm
from django.views.decorators.http import require_POST


@require_POST
def add_to_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart = Cart(request)
    form = CartForm(data=request.POST)
    if form.is_valid():
        quantity = form.cleaned_data["quantity"]
        replace = form.cleaned_data["replace"]
        cart.add(movie, quantity, replace)
    return redirect("cart_detail")


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item["refresh_form"] = CartForm(initial={
            "quantity": item["quantity"],
            "replace": True,
        })
    return render(request, "cart/cart_detail.html", context={
        "cart": cart,
    })


def remove_from_cart(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    cart = Cart(request)
    cart.remove(movie)
    cart.save()
    return redirect("cart_detail")

@require_POST
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")
