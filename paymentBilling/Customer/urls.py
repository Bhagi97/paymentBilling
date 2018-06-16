from .resources import *
from django.conf.urls import url
from django.urls import path, include
from tastypie.api import Api
from . import views

c_api = Api(api_name='api')
c_api.register(CustomerResource())
c_api.register(InvoiceResource())


urlpatterns = [
    path('api/', include(c_api.urls)),  # 127.0.0.1:8000/customer/api/
    # path('api/', include(InvoiceResource().urls)),

]
