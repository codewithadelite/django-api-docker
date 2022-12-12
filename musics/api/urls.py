from django.urls import path
from . import rest

urlpatterns = [
    path("", rest.MusicAPIView.as_view()),
    path("<int:pk>", rest.MusicDetailsAPIView.as_view()),
]
