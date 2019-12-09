from django.contrib import admin
from django.urls import path, include

from base.views import (
    registration_view,
    base,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration_view, name="register"),
    path('', base, name="home"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
]
