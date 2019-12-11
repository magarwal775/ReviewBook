from django.contrib import admin
from django.urls import path, include

from base.views import (
    base,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name="home"),
    path('', include('accounts.urls')),
    path('', include('base.urls')),
]
