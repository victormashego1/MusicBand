from django.urls import path
from . import views

app_name = "musicband"
urlpatterns = [
    path("", views.index, name="index"),
    path("records/", views.records, name="records"),
    path("about/", views.about, name="about"),
    path("<int:music_id>/", views.detail, name="detail"),
    path("<int:music_id>/vote/", views.vote, name="vote"),
    path('', views.musicband, name='musicband'),
]