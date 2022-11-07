from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def my_place(request):
    return render(request,'myservice/my_place.html')

def home(request):
    return render(request,'myservice/project-첫화면.html')

def login(request):
    return render(request,'myservice/log_in.html')