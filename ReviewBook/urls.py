from django.contrib import admin
from django.urls import path, include

from base.views import (
    registration_view,
    base,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('', base, name="home"),
]
