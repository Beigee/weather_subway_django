from django.urls import path
from . import views

urlpatterns = [
    path('date_opt/',  views.date_opt, name='date_opt'),
    path('date_opt/subway_opt', views.subway_opt, name='subway_opt'),
]