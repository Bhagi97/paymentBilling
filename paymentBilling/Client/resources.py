from tastypie.resources import ModelResource
from tastypie import fields

from .models import Client, Profile
from tastypie.authorization import Authorization


class ClientResource(ModelResource):
    profiles = fields.ToManyField('Client.resources.ProfileResource', 'profile', full=True, null=True)

    class Meta:
        queryset = Client.objects.all()
        resource_name = 'client'
        authorization = Authorization()


class ProfileResource(ModelResource):
    client = fields.ToOneField('Client.resources.ClientResource', 'client')

    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'
        authorization = Authorization()