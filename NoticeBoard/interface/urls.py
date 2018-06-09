from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login_request, name='login'),
    url(r'^logout$', views.logout_request, name='logout'),
    url(r'^ajax/getposterdetails/$', views.getposterdetails, name='getposterdetails'),
    url(r'^ajax/updateposter/$', views.updateposter, name='updateposter'),
    url(r'^ajax/deleteposter/$', views.deleteposter, name='deleteposter'),
]