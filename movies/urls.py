from django.urls import path
from movies.views import(
    give_movie_review,
    select_movie,
    index,
    details,
    review_detail,
)

app_name='movies'

urlpatterns = [
    path('review/movie/<int:movie_id>', give_movie_review, name="give_movie_review" ),
    path('selectmovie/', select_movie, name="select_movie" ),
    path('<slug>/', review_detail, name="review_detail"),
    path('', index, name="index"),
    path('<int:movie_id>', details, name="details"),
]
