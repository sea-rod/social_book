from django.urls import path
from .views import index, signup, login, logout, settings, upload


urlpatterns = [
    path("", index, name="index"),
    path("settings/", settings, name="settings"),
    path("signup/", signup, name="signup"),
    path("signin/", login, name="signin"),
    path("logout/", logout, name="logout"),
    path("upload/", upload, name="upload"),
]
