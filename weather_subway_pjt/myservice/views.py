from django.shortcuts import render
from .models import MyPlace
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:log_in')
def my_place(request):
    
    station = request.GET['station']
    location = request.GET.getlist('location')
    id = request.user.id
    for name in location:
        MyPlace(id=id, station_name=station, t_name=name, cate=request.GET[name]).save()

    # context = {'statoin_name':my_place.station_name.values, 't_name':my_place.t_name.values, 'cate':my_place.cate.values }

    return render(request, 'myservice/my_place.html')