from django.urls import path
from .views import uploadImg, showImg

urlpatterns = [
    path('uploadImg', uploadImg),
    path('showImg', showImg)
]