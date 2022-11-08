#options->views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def date_opt(request):
	return render(request, 'options/date_opt.html')

def subway_opt(request):
	return render(request, 'options/subway_opt.html')

def place_opt(request):
	return render(request, 'options/place_opt.html')