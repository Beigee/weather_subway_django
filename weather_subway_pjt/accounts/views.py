from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms import UserForm


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'templates/sign_up.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password1', None)

#         me = auth.authenticate(request, username=username, password=password)
#         # auth.authenticate() 로 암호화된 데이터베이스를 추가적인 코드없이 조회 및 검증이 가능
        
#         if me is not None:  # 입력한 정보가 존재하고 일치한다면
#             auth.login(request, me)  # auth.login() 으로 토큰을 생성 및 전달
#             return redirect('/') # 메인페이지로 이동
#         else:  # 입력한 정보가 없거나 틀리다면
#             return redirect('/log_in')  # 페이지 다시 로드
#     elif request.method == 'GET':
#         return render(request, 'accounts/log_in.html')
