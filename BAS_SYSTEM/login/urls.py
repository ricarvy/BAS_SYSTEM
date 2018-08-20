from django.urls import path

from .views import index, login
from image_collection.views import uploadImg

urlpatterns = [
    path('', index),
    path('login',login),
    path('uploadImg', uploadImg)
]