from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import ImageCollectionImg, Provincial, City, DcyDelivery
import os
import time
import random

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/') # media即为图片上传的根路径
MEDIA_URL = '/media/'

@csrf_exempt
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        province_name = request.POST.get('province_name')
        city_name = request.POST.get('city_name')
        img_url = request.FILES.get('img')
        # 生成时间戳
        tag = str(round(time.time() * 1000)) + str(random.randint(0, 100000000))
        if img_url is not None:
            img = ImageCollectionImg(img_url = tag + '.jpg',
                                     company_name = company_name,
                                     province_name = province_name,
                                     city_name = city_name)
            img.save()
            destination = open('E:/'+ tag +'.jpg', 'wb+')
            for chunk in img_url.chunks():
                destination.write(chunk)
            destination.close()

    return render(request, 'imgUpload.html', {'provincial': Provincial.objects.all(),
                                              'city': City.objects.all(),
                                              'dcyDelivery': DcyDelivery.objects.all()})