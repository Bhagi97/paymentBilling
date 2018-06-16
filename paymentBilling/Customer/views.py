from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Customer
from .tables import CustomerTable
# Create your views here.

#
# def customers(request):
#     table = CustomerTable(Customer.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'export_details.html', {'table': table})

