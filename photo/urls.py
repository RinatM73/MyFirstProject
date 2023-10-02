from django.urls import path
from . import views

urlpatterns = [
    path('photo/', views.photoview, name = 'photo'),
]
