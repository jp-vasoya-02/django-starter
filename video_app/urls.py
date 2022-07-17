from django.urls import path
from video_app.views import *

urlpatterns = [
    path('',Home,name='index'),
]