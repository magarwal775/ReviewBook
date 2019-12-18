from django import forms

from movies.models import MovieReview, Movie

class GiveReviewForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = ['title', 'body', 'rating']

class UpdateReviewForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = ['title', 'body', 'rating']

    def save(self, commit=True):
        review = self.instance
        review.title = self.cleaned_data['title']
        review.body = self.cleaned_data['body']
        review.rating = self.cleaned_data['rating']

        if commit:
            review.save()

        return review
