from django.shortcuts import render
from .models import Fcuser
from django.http import HttpResponse


# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        rePassword = request.POST.get('rePassword', None)
        email = request.POST.get('email', None)

        err_res = {}

        if not (username and password and rePassword):
            blank = ''
            if username is None:
                blank = 'username'
            elif password is None:
                blank = 'password'
            elif rePassword is None:
                blank = 'rePassword'

            err_res['error'] = blank + '을 입력해주세요!'
        elif password != rePassword:
            err_res['error'] = '잘못된 비밀번호!'
        else:
            fcuser = Fcuser(
                username=username,
                password=password,
                user_email=email
            )

            fcuser.save()

        return render(request, 'register.html', err_res)
