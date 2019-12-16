from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from base.views import (
    base,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name="home"),
    path('', include('accounts.urls')),
    path('', include('base.urls')),
    path('movies/',include('movies.urls')),
    path('games/',include('games.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
