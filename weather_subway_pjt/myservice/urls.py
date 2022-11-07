from django.urls import path
from . import views



urlpatterns = [
    path('myplace',views.my_place),
    path('home',views.home),
    path('login',views.login)
]