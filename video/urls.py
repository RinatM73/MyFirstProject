from django.urls import path
from .views import *

urlpatterns = [
    path('video/', videoview, name = 'video'),
]