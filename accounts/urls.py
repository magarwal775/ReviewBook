from django.urls import path, include

from accounts.views import (
        registration_view,
        logout_view,
        login_view,
        must_authenticate_view,
        account_view,
        feed_view,
)

app_name='accounts'


urlpatterns = [
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('must_authenticate', must_authenticate_view, name="must_authenticate"),
    path('profile/', account_view, name="account_view"),
    path('feed/',feed_view, name="feed_view"),
]
