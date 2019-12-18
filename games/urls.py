from django.urls import path
from games.views import(
    give_game_review,
    select_game,
    index,
    details,
    review_detail,
    edit_review,
)

app_name='games'

urlpatterns = [
    path('review/game/<int:game_id>', give_game_review, name="give_game_review" ),
    path('selectgame/', select_game, name="select_game" ),
    path('<int:game_id>/', details, name='details'),
    path('<slug>/', review_detail, name="review_detail"),
    path('<slug>/edit', edit_review, name="edit_review"),
    path('', index,name='index'),
]
