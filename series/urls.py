from django.urls import path

from series.views import(
    give_episode_review,
    select_series,
    select_episode,
    review_detail,
)

app_name='series'

urlpatterns = [
    path('review/episode/<int:episode_id>', give_episode_review, name="give_episode_review" ),
    path('selectseries/', select_series, name="select_series" ),
    path('selectseries/selectepisode/<int:series_id>/', select_episode, name="select_episode"),
    path('<slug>/', review_detail, name="review_detail"),
]
