from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render
from NewHouse.models import NewHouse
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
            newHouseList = NewHouse.objects.all()
            #当前页码，显示几个页码，总数，一页显示几条
            paginator = CustomPaginator(current_page, 7, newHouseList, per_pager_num)
            try:
                posts = paginator.page(current_page)
            except PageNotAnInteger:
                posts = paginator.page(1)
            except EmptyPage:
                posts = paginator.page(paginator.num_pages)
            posts = serializers.serialize('json',posts)
            return HttpResponse(posts,'application/json')
            # return JsonResponse({
            #     'code': '200',
            #     'msg': '获取数据成功',
            #     'data': posts
            # })
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
            newhouse = NewHouse()
            newhouse.community = content['name']
            newhouse.city_area = content['area']
            newhouse.address = content['address']
            newhouse.house_type = content['type']
            newhouse.average_price = content['price']
            newhouse.house_square = content['square']
            newhouse.save()

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
    if (request.method == 'DELTE'):
        try:
            content = json.loads(request.body)
            newhouse = NewHouse.objects.get(pk=content['nid'])
            newhouse.delete()

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
            # body_unicode = request.body.decode('utf-8')
            # body = json.loads(body_unicode)
            # content = body['content']
            # content = json.loads(request.body)
            global content
            content=request.POST
            a = content.get('name')
            b = content.get('address')
            c = content.get('area')
            d = content.get('minPrice')
            e =content.get('maxPrice')
            newHouseList = NewHouse.objects.filter(community__contains=content.get('name'),
                                                   address__contains=content.get('address'),)
                                                   # city_area__contains=content.get('area'),
                                                   # average_price__gte=content.get('minPrice'),
                                                   # average_price__lte=content.get('maxPrice')

            current_page = content.get('curpage')
            per_pager_num = content.get('pageSize')
            # 当前页码，显示几个页码，总数，一页显示几条
            paginator = CustomPaginator(current_page, 7, newHouseList, per_pager_num)
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


#对新房中的数据按照区域划分
# def myChart2(request):
#     if(request.method=='POST'):
#         try:
#             content=json.loads(request.body)
#             areaList=NewHouse.objects.get(city_area=content['area'])
#             countList=NewHouse.objects.get(areaList).