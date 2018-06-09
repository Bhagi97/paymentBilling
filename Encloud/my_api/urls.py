from django.conf.urls import url, include
from django.contrib import admin
from my_api.resources import *

urlpatterns = [
    url(r'timestampdb/', include(TimestampResource().urls)),
    url(r'franchise/', include(FranchiseResource().urls)),
    url(r'package/', include(PackageResource().urls)),
    url(r'packagemask/', include(PackageMaskResource().urls)),
    url(r'service/', include(ServiceResource().urls)),
    url(r'servicemask/', include(ServiceMaskResource().urls)),
    url(r'treatment/', include(TreatmentResource().urls)),
    url(r'treatmentmaster/', include(TreatmentMasterResource().urls)),
    url(r'discount/', include(DiscountResource().urls)),
    url(r'country/', include(CountryResource().urls)),
    url(r'state/', include(StateResource().urls)),
    url(r'district/', include(DistrictResource().urls)),
    url(r'town/', include(TownResource().urls)),
    #url(r'note/', include(NoteResource().urls)),
    url(r'enquiry/', include(EnquiryResource().urls)),
    ]
