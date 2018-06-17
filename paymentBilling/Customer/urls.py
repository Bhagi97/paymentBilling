from .resources import *
from django.conf.urls import url, include
from tastypie.api import Api
from . import views

c_api = Api(api_name='api')
c_api.register(CustomerResource())
c_api.register(InvoiceResource())
c_api.register(UserResource())


urlpatterns = [
    # 127.0.0.1:8000/customer/api/
    url(r'^api/', include(c_api.urls)),

]
