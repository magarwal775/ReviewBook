from django import forms

from movies.models import MovieReview, Movie

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = ['title', 'body', 'rating']
