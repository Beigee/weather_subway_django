#options->views.py
from django.shortcuts import render
from django.http import HttpResponse
from options import module_test
# Create your views here.
def date_opt(request):
	return render(request, 'options/date_opt.html')

def subway_opt(request):
	# 1. get 방식으로 넘어온 date, time, gu 값 가지고 오기(변수로) # 게시판 데이터, 카페 장고
	weather,result = module_test.weather_import(day, time, gu) # view에서 호출
	print(weather, result)


	return render(request, 'options/subway_opt.html')

def place_opt(request):
	return render(request, 'options/place_opt.html')
