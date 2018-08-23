from django.urls import path
from .views import uploadImg

urlpatterns = [
    path('uploadImg', uploadImg),
]