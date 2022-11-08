#options->views.py
from django.shortcuts import render
from django.http import HttpResponse
from options import module_test
# Create your views here.
def date_opt(request):
	return render(request, 'options/date_opt.html')

def subway_opt(request):
	day = request.GET['day']
	time = request.GET['time']
	gu = request.GET['gu']
	# 1. get 방식으로 넘어온 date, time, gu 값 가지고 오기(변수로) # 게시판 데이터, 카페 장고
	weather,result = module_test.weather_import(day = day, time = time, gu = gu) # view에서 호출
	# 딕셔너리로 변환,weather{tmp:weather.ONDO}

	context = {'tmp': weather.ONDO.iloc[0], 'humn': weather.HUMN.iloc[0], 'sky': weather.SKY.iloc[0], 'rain': weather.RAIN.iloc[0],
			   'snow': weather.SNOW.iloc[0], 'windd': weather.WINDD.iloc[0], 'winds': weather.WINDS.iloc[0]}
	print(weather.ONDO.iloc[0])
	return render(request,  'options/subway_opt.html', {'weather':context})
	# content = {'categories': categories, 'rests': rest}
	# return render(request, 'sharesRes/restaurantUpdate.html', content)
	# return render(request, 'options/subway_opt.html') # render할때 context를 붙여서 보내기!


def place_opt(request):
	return render(request, 'options/place_opt.html')
