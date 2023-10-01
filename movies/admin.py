from django.contrib import admin
from .models import Movie, Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "description", "price", "running_time",
                    "genre", "cover")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("movie", "user", "datetime_created", "datetime_modified", "text", "recommend")
