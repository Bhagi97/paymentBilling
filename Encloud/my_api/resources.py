from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
from app.models import *
from tastypie.constants import ALL

import ast
from functools import reduce
import pdb


class SillyAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        try:
            if request.META['HTTP_API'] == 'ANJBLXA5vIxxSefdxEOLkgud4SXASZoa':
                return True
        except:
            pass
        # Wrong API
        return False


class SillyAuthorization(Authorization):
    def read_list(self, object_list, bundle):
        return object_list.all()

    def read_detail(self, object_list, bundle):
        return True

    def create_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def create_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def update_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def update_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def delete_list(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

    def delete_detail(self, object_list, bundle):
        raise Unauthorized("Sorry, no deletes.")

class FranchiseResource(ModelResource):
    class Meta:
        queryset = Franchise.objects.all()
        resource_name = 'franchise'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        filtering = {'state': ALL, 'country': ALL, 'district': ALL, 'town': ALL, }


class ServiceResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Service.objects.all()
        resource_name = 'service'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        filtering = {'body_part':ALL,}

    def apply_filters(self, request, applicable_filters):
        my_data = self.get_object_list(request).filter(**applicable_filters)
        try:
            if request.GET['relevant']:
                masks = map(lambda x: ast.literal_eval('0b'+x), ServiceMask.objects.all().values_list('mask',flat=True))
                mask = reduce((lambda x, y: x | y), masks)
                for obj in my_data:
                    if not (mask & (1 << obj.id)):
                        my_data = my_data.exclude(id=obj.id)
        except KeyError:
            pass
        return my_data


# Helper to decide exclusion
def exclude(f, obj, request):
    # pid/sid
    try:
        if request.GET['pid']:
            if obj.mask[int(request.GET['pid']) - 1] == '0':
                return 1
    except:
        try:
            if request.GET['sid']:
                if obj.mask[int(request.GET['sid']) - 1] == '0':
                    return 1
        except:
            pass

    # type
    try:
        if not (f.franchise_type == request.GET['type']):
            return 1
    except:
        pass

    # country
    try:
        if not (f.country == request.GET['country']):
            return 1
    except:
        pass
    # state
    try:
        if not (f.state == request.GET['state']):
            return 1
    except:
        pass
    # city
    try:
        if not (f.district == request.GET['district']):
            return 1
    except:
        pass
    # town
    try:
        if not (f.town == request.GET['town']):
            return 1
    except:
        pass

    return 0


class ServiceMaskResource(ModelResource):
    class Meta:
        limit = 0
        queryset = ServiceMask.objects.all()
        resource_name = 'servicemask'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()

    def apply_filters(self, request, applicable_filters):
        my_data = self.get_object_list(request).filter(**applicable_filters)
        for obj in my_data:
            f = Franchise.objects.get(id=int(obj.franchise_code))
            if exclude(f, obj, request):
                my_data = my_data.exclude(id=obj.id)
        return my_data

    def dehydrate(self, bundle):
        f = Franchise.objects.get(id=int(bundle.data['franchise_code']))
        bundle.data['franchise_name'] = f.franchise_name
        return bundle


class PackageResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Package.objects.all()
        resource_name = 'package'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()

    def apply_filters(self, request, applicable_filters):
        my_data = self.get_object_list(request).filter(**applicable_filters)
        try:
            if request.GET['relevant']:
                masks = map(lambda x: ast.literal_eval('0b'+x), PackageMask.objects.all().values_list('mask',flat=True))
                mask = reduce((lambda x, y: x | y), masks)
                for obj in my_data:
                    if not (mask & (1 << obj.id)):
                        my_data = my_data.exclude(id=obj.id)
        except KeyError:
            pass
        return my_data



class PackageMaskResource(ModelResource):
    class Meta:
        limit = 0
        queryset = PackageMask.objects.all()
        resource_name = 'packagemask'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()

    def apply_filters(self, request, applicable_filters):
        my_data = self.get_object_list(request).filter(**applicable_filters)
        for obj in my_data:
            f = Franchise.objects.get(id=int(obj.franchise_code))
            if exclude(f, obj, request):
                my_data = my_data.exclude(id=obj.id)
        return my_data

    def dehydrate(self, bundle):
        f = Franchise.objects.get(id=int(bundle.data['franchise_code']))
        bundle.data['franchise_name'] = f.franchise_name
        return bundle



class TreatmentResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Treatment.objects.all()
        resource_name = 'treatment'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        filtering = {'name': ALL, }

    def apply_filters(self, request, applicable_filters):
        my_data = self.get_object_list(request).filter(**applicable_filters)
        try:
            if request.GET['relevant']:
                my_data = my_data.values('name').distinct()
        except:
            f= Franchise.objects.all()
            try:
                f = f.filter(country=request.GET['country'])
            except:
                pass
            try:
                f = f.filter(state=request.GET['state'])
            except:
                pass
            try:
                f = f.filter(district=request.GET['district'])
            except:
                pass
            try:
                f = f.filter(franchise_type=request.GET['type'])
            except:
                pass
            my_data = my_data.filter(franchise_code__in=f.values('id'))
        return my_data

    def dehydrate(self, bundle):
        f = Franchise.objects.get(id=int(bundle.data['franchise_code']))
        bundle.data['franchise_name'] = f.franchise_name
        return bundle


class TreatmentMasterResource(ModelResource):
    class Meta:
        limit = 0
        queryset = TreatmentMaster.objects.all()
        resource_name = 'treatmentmaster'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()


class EnquiryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Enquiry.objects.all()
        resource_name = 'enquiry'
        authentication = SillyAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        if 'date' in bundle.data and 'time' in bundle.data:
            bundle.data['requested_time'] = datetime.strptime(bundle.data['date']+"|"+bundle.data['time'], "%Y-%m-%d|%H:%M:%S")
        elif 'date' in bundle.data:
            bundle.data['requested_time'] = datetime.strptime(bundle.data['date'],"%Y-%m-%d")
        return bundle


class CountryResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Franchise.objects.all()
        resource_name = 'country'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        fields = ['country']
        include_resource_uri = False

    def apply_filters(self, request, applicable_filters):
        countries = []
        my_data = self.get_object_list(request).filter(**applicable_filters)
        i,size = 0,len(my_data)
        while i<size:
            if my_data[i].country in countries:
                my_data = my_data.exclude(id=my_data[i].id)
                size-=1
            else:
                countries.append(my_data[i].country)
                i+=1
        return my_data


class StateResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Franchise.objects.all()
        resource_name = 'state'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        fields = ['country','state']
        include_resource_uri = False
        filtering = {"country":ALL,}

    def apply_filters(self, request, applicable_filters):
        states = []
        my_data = self.get_object_list(request).filter(**applicable_filters)
        i,size = 0,len(my_data)
        while i<size:
            if my_data[i].state in states:
                my_data = my_data.exclude(id=my_data[i].id)
                size-=1
            else:
                states.append(my_data[i].state)
                i+=1
        return my_data


class DistrictResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Franchise.objects.all()
        resource_name = 'district'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        fields = ['country','state','district']
        include_resource_uri = False
        filtering = {'country': ALL,
                     'state': ALL,}

    def apply_filters(self, request, applicable_filters):
        districts = []
        my_data = self.get_object_list(request).filter(**applicable_filters)
        i,size = 0,len(my_data)
        while i<size:
            if my_data[i].district in districts:
                my_data = my_data.exclude(id=my_data[i].id)
                size-=1
            else:
                districts.append(my_data[i].district)
                i+=1
        return my_data


class TownResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Franchise.objects.all()
        resource_name = 'town'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()
        fields = ['country','state','district','town']
        include_resource_uri = False
        filtering = {'country': ALL,
                     'state': ALL,
                     'district': ALL,}

    def apply_filters(self, request, applicable_filters):
        towns = []
        my_data = self.get_object_list(request).filter(**applicable_filters)
        i,size = 0,len(my_data)
        while i<size:
            if my_data[i].town in towns:
                my_data = my_data.exclude(id=my_data[i].id)
                size-=1
            else:
                towns.append(my_data[i].town)
                i+=1
        return my_data


class TimestampResource(ModelResource):
    class Meta:
        limit = 0
        queryset = TimestampDB.objects.all()
        resource_name = 'timestampdb'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()


class DiscountResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Discount.objects.filter(subject='Service') | Discount.objects.filter(subject='Package')
        resource_name = 'discount'
        authentication = SillyAuthentication()
        authorization = SillyAuthorization()



class NoteResource(ModelResource):
    class Meta:
        limit = 0
        queryset = Note.objects.all()
        resource_name = 'note'
        authentication = SillyAuthentication()
        authorization = Authorization()