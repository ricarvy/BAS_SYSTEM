from django.shortcuts import render, reverse
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo, Provincial, City, DcyDelivery
from django.http import HttpResponseRedirect

# Create your views here.

@csrf_exempt
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    logined = False
    context = dict()
    if request.method == 'POST':
        username = request.POST.get('form-username')
        password = request.POST.get('form-password')
        userInfo = UserInfo.objects.filter(username=username)
        if len(userInfo) != 0 and list(userInfo.values())[0]['password'] == password:
            logined = True
            request.session['username'] = list(userInfo.values())[0]['username']
            request.session['permission'] = list(userInfo.values())[0]['permission_id']
            return render(request, 'imgUpload.html', {'permission': request.session.get('permission'),
                                                      'provincial': Provincial.objects.all(),
                                                      'provincial_list': list(Provincial.objects.all().values()),
                                                      'city': City.objects.all(),
                                                      'city_list' : list(City.objects.all().values()),
                                                      'dcyDelivery': DcyDelivery.objects.all()})
        else:
            return render(request, 'index.html', {'failed' : True})

