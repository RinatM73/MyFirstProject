from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.videoview, name = 'video'),
    path('<int:pk>', views.video_det, name = 'video_det'),
]