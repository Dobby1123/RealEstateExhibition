from django.http import HttpResponse
from django.shortcuts import render
from User.models import User
# Create your views here.
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from django.views.decorators.http import require_http_methods
def checkLogin(request):
    if (request.method == 'POST'):
        try:
            user = User.objects.filter(name=request.POST.get('username'),password=request.POST.get('password'))
            if user:
                return JsonResponse({
                    'code': '200',
                    'msg': '获取数据成功',
                    'data': user
                })
        except Exception as e:
            return JsonResponse({
                'code': '500',
                'msg': '获取失败',
            })
    else:
        return JsonResponse({
            'code': '302',
            'msg': '非法访问！',
        })

# def save(request):
#     user = User()
#     user.name = 'zzy'
#     user.password = '123456'
#     user.save()
#     return HttpResponse("!!!")