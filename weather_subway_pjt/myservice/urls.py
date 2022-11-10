from django.urls import path
from . import views



urlpatterns = [
    path('my_place/', views.my_place, name='my_place'),
]