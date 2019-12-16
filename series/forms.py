from django import forms

from series.models import EpisodeReview

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model=EpisodeReview
        fields = ['title', 'body', 'rating']
