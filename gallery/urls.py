from django.urls import path

from . import views

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    path('upload/', views.upload_video, name='upload_video'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
]
