from django.shortcuts import render

# Create your views here.
def date_opt(request):
    return render(request, 'options/date_opt_test5.html')

def subway_opt(request):
    return render(request,'options/subway_opt.html')