from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name ='home-page'),
    path('services/', Services, name ='services'),
    path('support/', Support, name ='support'),
]

