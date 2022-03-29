from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("frog-news", views.frog_news, name="frog_news"),
    path("eagle-news", views.eagle_news, name="eagle_news"),
    path("wolf-news", views.wolf_news, name="wolf_news"),
]
