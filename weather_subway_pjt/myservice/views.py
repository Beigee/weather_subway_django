from django.shortcuts import render
from django.http import HttpResponse
from .models import MyPlace


# Create your views here.
def my_place(request):
    
    station = request.GET['station']
    location = request.GET.getlist('location')
    id = request.user.id

    for name in location:
        MyPlace(id=id, station_name=station, t_name=name, cate=request.GET[name]).save()


    return render(request, 'myservice/my_place.html')
