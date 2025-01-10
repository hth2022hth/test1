from django.http import HttpResponse
from django.shortcuts import render

from wms.models import Users


def login(request):
    if request.method == "POST":

        usm = request.POST.get('usm')
        pwd = request.POST.get('pwd')
        error_msg = '用户名或密码错误'

        if Users.objects.filter(username=usm):
            if Users.objects.filter(username=usm)[0].password == pwd:
                return render(request, 'wms/base.html')
            else:

                return render(request, 'wms/login.html', {'error_msg': error_msg})
        else:
            return render(request, 'wms/login.html', {'error_msg': error_msg})
    return render(request, 'wms/login.html')
