from django.urls import path
from .views import hello_world, webcam_feed, webcam_view

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('webcam/', webcam_feed, name='webcam_feed'),
    path('webcam-view/', webcam_view, name='webcam_view'),
]
