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
        print(list(userInfo.values())[0]['password'])
        if len(userInfo) != 0 and list(userInfo.values())[0]['password'] == password:
            logined = True
            context['username'] = username
            return render(request, 'imgUpload.html', {'username': username,
                                                      'provincial': Provincial.objects.all(),
                                                      'provincial_list': list(Provincial.objects.all().values()),
                                                      'city': City.objects.all(),
                                                      'city_list' : list(City.objects.all().values()),
                                                      'dcyDelivery': DcyDelivery.objects.all()})
        else:
            return render(request, 'index.html', {'failed' : True})

