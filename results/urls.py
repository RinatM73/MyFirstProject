from django.urls import path
from .views import *

urlpatterns = [
    path('results/', resultsview, name = 'results'),
]