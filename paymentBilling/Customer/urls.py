from .resources import *
from tastypie.api import Api
from django.conf.urls import url, include

c_api = Api(api_name='api')
c_api.register(CustomerResource())
c_api.register(InvoiceResource())

urlpatterns = [
    url(r'^api/', include(c_api.urls))  # 127.0.0.1:8000/customer/api/api/
]

# FOR CUSTOMER
# http://127.0.0.1:8000/customer/api/api/customer/?format=json

# FOR INVOICE
# http://127.0.0.1:8000/customer/api/api/invoice/?format=json