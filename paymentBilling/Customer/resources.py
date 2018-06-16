from tastypie.resources import ModelResource
from tastypie import fields
from .models import Customer, Invoice
from tastypie.authorization import Authorization


class CustomerResource(ModelResource):
    invoice_details = fields.ToManyField('Customer.resources.InvoiceResource', 'pending', full=True, null=True)

    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
        authorization = Authorization()


class InvoiceResource(ModelResource):
    customer = fields.ToOneField('Customer.resources.CustomerResource', 'customer')
    # customer = fields.ForeignKey(CustomerResource, 'customer')
    class Meta:
        queryset = Invoice.objects.all()
        resource_name = 'invoice'
        authorization = Authorization()

