from django import forms

from games.models import GameReview, Game

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model=GameReview
        fields = ['title', 'body', 'rating']
