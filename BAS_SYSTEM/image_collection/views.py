from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import ImageCollectionImg, Provincial, City, DcyDelivery
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import os
import time
import random
from PIL import Image

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'static\\media').replace('\\', '/') # media即为图片上传的根路径
MEDIA_URL = '/media/'

def turn_midImg_to_img(midImg):
    im_pic = Image.open(midImg)
    w, h = im_pic.size
    if w >= h:
        w_start = (w - h) * 0.618
        box = (w_start, 0, w_start + h, h)
        region = im_pic.crop(box)
    else:
        h_start = (h - w) * 0.618
        box = (0, h_start, w, h_start + w)
        region = im_pic.crop(box)
    pic_io = BytesIO()
    region.save(pic_io, im_pic.format)
    pic_file = InMemoryUploadedFile(
        file=pic_io,
        field_name=None,
        name=midImg.name,
        content_type=midImg.content_type,
        size=midImg.size,
        charset=None
    )
    return pic_file

@csrf_exempt
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        province_name = request.POST.get('province_name')
        city_name = request.POST.get('city_name')
        img_url = request.FILES.get('img')
        print(type(img_url))
        # 生成时间戳
        tag = str(round(time.time() * 1000)) + str(random.randint(0, 100000000))
        if img_url is not None:
            img = ImageCollectionImg(img_url = tag + '.jpg',
                                     company_name = company_name,
                                     province_name = province_name,
                                     city_name = city_name,
                                     upload_username = request.session.get('username','None'),
                                     timestamp = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            img.save()
            # destination = open(os.getcwd()+'\\img\\'+ tag +'.jpg', 'wb+')
            destination = open(os.path.join(MEDIA_ROOT, tag+'.jpg').replace('\\', '/'), 'wb+')
            for chunk in img_url.chunks():
                destination.write(chunk)
            destination.close()

    return render(request, 'imgUpload.html', {'permission': request.session.get('permission'),
                                              'provincial': Provincial.objects.all(),
                                              'city': City.objects.all(),
                                              'dcyDelivery': DcyDelivery.objects.all()})
@csrf_exempt
def showImg(request):
    page_account = 0
    image_num_per_page = 1
    path = BASE_DIR + '/static/media'
    imageList = os.listdir(path)
    print(os.listdir(path))
    return render(request, 'img_detail.html',{'imageList':imageList,
                                              'page_account': page_account,
                                              'image_num_per_page':image_num_per_page})