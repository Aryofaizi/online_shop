from movies.models import Movie


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.cart = self.session.get("cart")
        if not self.cart:
            self.cart = self.session["cart"] = {}

    def add(self, movie, quantity, replace=False):
        movie_id = str(movie.id)
        if movie_id not in self.cart:
            self.cart[movie_id] = {"quantity": 0}
        if replace:
            self.cart[movie_id]["quantity"] = quantity
        else:
            self.cart[movie_id]["quantity"] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, movie):
        movie_id = str(movie.id)
        if movie_id in self.cart:
            del self.cart[movie_id]

    def __iter__(self):
        ids = self.cart.keys()
        movies = Movie.objects.filter(id__in=ids)
        cart = self.cart.copy()
        for movie in movies:
            cart[str(movie.id)]["movie_obj"] = movie
            cart[str(movie.id)]["total_quantity_price"] = movie.price * cart[str(movie.id)]["quantity"]

        for item in cart.values():
            yield item

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())

    def clear(self):
        del self.session["cart"]

    def total_price(self):
        return sum(item["quantity"] * item["movie_obj"].price for item in self.cart.values())