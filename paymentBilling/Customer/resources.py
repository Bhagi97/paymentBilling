from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from .models import Customer, Invoice, Receipt
from tastypie.authorization import Authorization


from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.utils import trailing_slash
from django.conf.urls import url

from import_export import resources


class ImportCustomerResource(resources.ModelResource):
    class Meta:
        model = Customer


class CustomerResource(ModelResource):
    invoice_details = fields.ToManyField('Customer.resources.InvoiceResource', 'invoice', full=True, null=True)
    profile = fields.ToOneField('Client.resources.ProfileResource', 'profile')

    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'
        authorization = Authorization()
        filtering = {'name': ALL, 'phone_no': ALL, 'id': ALL}


class InvoiceResource(ModelResource):
    customer = fields.ToOneField('Customer.resources.CustomerResource', 'customer')
    # customer = fields.ForeignKey(CustomerResource, 'customer')
    client = fields.ToOneField('Client.resources.ClientResource', 'client')

    class Meta:
        queryset = Invoice.objects.all()
        resource_name = 'invoice'
        authorization = Authorization()
        filtering = {
            "id": ALL,
            "customer": ALL_WITH_RELATIONS,
            "client": ALL_WITH_RELATIONS
        }


class ReceiptResource(ModelResource):
    profile = fields.ToOneField('Client.resources.ProfileResource', 'profile')
    client = fields.ToOneField('Client.resources.ClientResource', 'client')
    customer = fields.ToOneField('Customer.resources.CustomerResource', 'customer')
    class Meta:
        queryset = Receipt.objects.all()
        resource_name = 'receipt'
        authorization = Authorization()
        filtering = {
            "id": ALL,
            "customer": ALL_WITH_RELATIONS,
            "profile": ALL_WITH_RELATIONS,
            "client": ALL_WITH_RELATIONS
        }


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name', 'email']
        allowed_methods = ['get', 'post']
        resource_name = 'user'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return self.create_response(request, {
                    'success': True
                })
            else:
                return self.create_response(request, {
                    'success': False,
                    'reason': 'disabled',
                    }, HttpForbidden )
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, { 'success': True })
        else:
            return self.create_response(request, { 'success': False }, HttpUnauthorized)