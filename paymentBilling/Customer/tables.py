import django_tables2 as tables
from .models import Customer


class CustomerTable(tables.Table):
    class Meta:
        model = Customer
