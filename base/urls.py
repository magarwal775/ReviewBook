from django.urls import path

from base.views import(
    base,
    home,
    select_category,
)

urlpatterns = [
    path('', home, name="home"),
    path('selectcategory/', select_category, name="select_category"),
]
