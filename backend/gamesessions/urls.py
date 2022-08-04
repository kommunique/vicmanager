from django.urls import path
from . import views

app_name = "gamesessions"

urlpatterns = [
    path("", views.home_page, name="homepage"),
]
