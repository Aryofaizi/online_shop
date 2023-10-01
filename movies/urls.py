from django.urls import path
from .views import MovieListView, MovieCreateView, MovieUpdateView,\
    movie_detail_view

urlpatterns = [
    path("list/", MovieListView.as_view(), name="movie_list"),
    path("create/", MovieCreateView.as_view(), name="movie_create"),
    path("update/<int:pk>", MovieUpdateView.as_view(), name="movie_update"),
    path("detail/<int:pk>/", movie_detail_view, name="movie_detail"),
]
