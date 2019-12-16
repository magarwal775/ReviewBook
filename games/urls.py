from django.urls import path

from . import views

app_name= 'games'

urlpatterns= [
    path('',views.index,name='index'),
    path('<int:game_id>/',views.details,name='details'),
]
