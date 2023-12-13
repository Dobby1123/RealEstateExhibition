from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render
from RentHouse.models import RentHouse
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
# 查询所有
from RealEstateExhibition.views import CustomPaginator

def select_all(request):
    if (request.method == 'POST'):
        try:
            current_page = request.POST.get('curPage')
            per_pager_num = request.POST.get('pageSize')
            rentList = RentHouse.objects.all()
            #当前页码，显示几个页码，总数，一页显示几条
            paginator = CustomPaginator(current_page, 7, rentList, per_pager_num)
            try:
                posts = paginator.page(current_page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            posts = serializers.serialize('json',posts)
            return HttpResponse(posts,'application/json')
        except Exception as e:
            print(e)
            return JsonResponse({
                'code': '500',
                'msg': '获取失败',
            })
    else:
        return JsonResponse({
            'code': '302',
            'msg': '非法访问！',
        })



#更新或者修改
def save_or_update(request):
    if (request.method == 'POST'):
        try:
            content = json.loads(request.body)
            rent = RentHouse()
            rent.rent_introduce=content["introduce"]
            rent.rent_address =content["address"]
            rent.rent_style=content["style"]
            rent.rent_square=content["square"]
            rent.rent_orientations=content["direction"]
            rent.month_price=content["mprice"]
            rent.save()

            return JsonResponse({
                'code': '200',
                'msg': '更新成功',
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                'code': '500',
                'msg': '获取失败',
            })
    else:
        return JsonResponse({
            'code': '302',
            'msg': '非法访问！',
        })


def delete(request):
    if (request.method == 'DELETE'):
        try:
            content = json.loads(request.body)
            rent = RentHouse.objects.get(pk=content['tid'])
            rent.delete()

            return JsonResponse({
                'code': '200',
                'msg': '删除成功',
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                'code': '500',
                'msg': '获取失败',
            })
    else:
        return JsonResponse({
            'code': '302',
            'msg': '非法访问！',
        })

#模糊查询
#新房查询前端字段：name小区名称 ，address 地址，area 地区
def select_by_pattern(request):
    if (request.method == 'POST'):
        try:
            content = json.loads(request.body)
            erList = RentHouse.objects.filter(rent_introduce__contains=content['introduce'],
                                                   rent_address__contains=content['address'],
                                                   month_price__gte=content['minPrice'],
                                                   month_price__lte=content['maxPrice'])

            current_page = content['curpage']
            per_pager_num = content['pageSize']
            # 当前页码，显示几个页码，总数，一页显示几条
            paginator = CustomPaginator(current_page, 7, erList, per_pager_num)
            try:
                posts = paginator.page(current_page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            posts = serializers.serialize('json', posts)
            return HttpResponse(posts, 'application/json')
        except Exception as e:
            print(e)
            return JsonResponse({
                'code': '500',
                'msg': '获取失败',
            })
    else:
        return JsonResponse({
            'code': '302',
            'msg': '非法访问！',
        })