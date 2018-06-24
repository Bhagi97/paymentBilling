from tastypie.resources import ModelResource, ALL
from tastypie import fields

from .models import Client, Profile
from tastypie.authorization import Authorization


class ClientResource(ModelResource):
    profiles = fields.ToManyField('Client.resources.ProfileResource', 'client_profile', full=True, null=True)

    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization = Authorization()
        filtering = {'id': ALL}


class ProfileResource(ModelResource):

    user = fields.ToOneField('Customer.resources.UserResource', 'user')
    client = fields.ToOneField('Client.resources.ClientResource', 'client')

    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'
        authorization = Authorization()
        filtering = {'id': ALL}