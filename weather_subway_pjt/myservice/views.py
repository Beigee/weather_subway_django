from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def my_place(request):


    return render(request, 'myservice/my_place.html')
