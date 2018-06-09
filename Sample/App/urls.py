from django.conf.urls import url, include
from django.contrib import admin
from resources import *

urlpatterns = [
    # The normal jazz here...
    url(r'^api/', include(UserResource().urls)),
]
