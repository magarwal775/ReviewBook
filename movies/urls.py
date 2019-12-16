from django.urls import path
from movies.views import(
    give_movie_review,
    select_movie,
)

urlpatterns = [
    path('review/movie/<int:movie_id>', give_movie_review, name="give_movie_review" ),
    path('selectmovie/', select_movie, name="select_movie" ),
]
