from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField


class Movie(models.Model):
    genre_choices = [
        ("Act", "action"),
        ("Com", "comedy"),
        ("Dra", "drama"),
        ("Hor", "horror"),
    ]
    title = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = RichTextField()
    # price = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.PositiveIntegerField()
    running_time = models.IntegerField()
    genre = models.CharField(max_length=3, choices=genre_choices)
    cover = models.ImageField(upload_to="covers/")

    class Meta:
        ordering = ("title", )


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name="comment")
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    recommend = models.BooleanField(default=False)
