from django.template import loader
from django.http import HttpResponse
import pdb
import datetime as dt
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from helper import *

def myint(x):
    if x == None:
        return 0
    else:
        return int(x)

@login_required(login_url='login.html')
def index(request):
    perm_list={}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename]=True
    context = {'permissions':perm_list}
    my_code = Profile.objects.get(user=request.user).franchise_code

    if my_code == 0:
        role = Profile.objects.get(user=request.user).role
        if role != 'Vendor':
            context['sales'] = myint(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum'])
            context['customers'] = myint(Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
            context['new_customers'] = myint(Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
            context['enquiries'] = len(Enquiry.objects.filter(timestamp__gte=dt.datetime.combine(dt.date.today(),dt.time.min)))
        else:
            context['sales'] = myint(Franchise.objects.filter(vendor__user=request.user).aggregate(Sum('sales_today'))['sales_today__sum'])
            context['customers'] = myint(Franchise.objects.filter(vendor__user=request.user).aggregate(Sum('customers_today'))['customers_today__sum'])
            context['new_customers'] = myint(Franchise.objects.filter(vendor__user=request.user).aggregate(Sum('new_customers'))['new_customers__sum'])
            context['enquiries'] = len(Enquiry.objects.filter(timestamp__gte=dt.datetime.combine(dt.date.today(), dt.time.min), franchise_code__in=list(Franchise.objects.filter(vendor__user=request.user).values_list('id',flat=True))))
    else:
        context['sales'] = myint(Franchise.objects.get(id=my_code).sales_today)
        context['customers'] = myint(Franchise.objects.get(id=my_code).customers_today)
        context['new_customers'] = myint(Franchise.objects.get(id=my_code).new_customers)
        context['enquiries'] = len(Enquiry.objects.filter(timestamp__gte=dt.datetime.combine(dt.date.today(), dt.time.min),franchise_code=my_code))
    template = loader.get_template('app/mydir/quicknav.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='login.html')
def gentella_html(request):
    perm_list = {}
    for x in Permission.objects.filter(user=request.user):
        perm_list[x.codename] = True
    context = {'permissions': perm_list}
    load_template = request.path.split('/')[-1]
    if load_template=='quicknav.html':
        my_code = Profile.objects.get(user=request.user).franchise_code

        if my_code == 0:
            context['sales'] = int(round(Franchise.objects.aggregate(Sum('sales_today'))['sales_today__sum']))
            context['customers'] = int(Franchise.objects.aggregate(Sum('customers_today'))['customers_today__sum'])
            context['new_customers'] = int(Franchise.objects.aggregate(Sum('new_customers'))['new_customers__sum'])
            context['enquiries'] = len(Enquiry.objects.filter(
                timestamp__gte=dt.datetime.combine(dt.date.today(), dt.time.min)))
        else:
            context['sales'] = int(round(Franchise.objects.get(id=my_code).sales_today))
            context['customers'] = int(Franchise.objects.get(id=my_code).customers_today)
            context['new_customers'] = int(Franchise.objects.get(id=my_code).new_customers)
            context['enquiries'] = len(Enquiry.objects.filter(
                timestamp__gte=dt.datetime.combine(dt.date.today(), dt.time.min),
                franchise_code=my_code))
    template = loader.get_template('app/mydir/'+load_template)
    return HttpResponse(template.render(context, request))


def err_404(request):
    template = loader.get_template('app/mydir/page_404.html')
    return HttpResponse(template.render({}, request))


def err_500(request):
    template = loader.get_template('app/mydir/page_500.html')
    return HttpResponse(template.render({}, request))