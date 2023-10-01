from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import Movie
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from .forms import MovieForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list.html"
    paginate_by = 2


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ("title", "user", "description", "price", "running_time", "genre", "cover")
    template_name = "movies/movie_create.html"
    success_url = reverse_lazy("movie_list")


class MovieUpdateView(UserPassesTestMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = "movies/movie_create.html"
    success_url = reverse_lazy("movie_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def handle_no_permission(self):
        return redirect("login")


@login_required
def movie_detail_view(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie_comment = movie.comment.all()
    form = CommentForm(request.POST)
    if request.POST:
        new_comment = form.save(commit=False)
        new_comment.movie = movie
        new_comment.user = request.user
        new_comment.save()
        return redirect("movie_detail", pk=movie.id)
    else:
        return render(request, "movies/movie_detail.html", context={
            "movie": movie,
            "comments": movie_comment,
            "form": form,
        })





