from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "user", "description", "price", "running_time",
                  "genre", "cover")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text", "recommend")
