from django.shortcuts import render
from django.http import HttpResponseRedirect
from Customer.models import Customer, Invoice
from Customer.forms import *
from django.db import IntegrityError
from tablib import Dataset
from .forms import *

from Customer.resources import ImportCustomerResource

from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.


def login_request(request):

    context, perm_list = {}, {}
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = LoginForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                for x in Permission.objects.filter(user=request.user):
                    perm_list[x.codename] = True
                context = {'permissions': perm_list}

                return render(request, 'ElaAdmin/index.html', context)

    else:
        form = LoginForm()
        return render(request, 'ElaAdmin/login.html', {'form': form})


@login_required(login_url='login.html')
def logout_request(request):
    logout(request)
    form = LoginForm()
    return render(request, 'ElaAdmin/login.html', {'form': form})


@login_required(login_url='login.html')
def index(request):
    return render(request, 'ElaAdmin/index.html')


def page_error(request):
    return render(request, 'ElaAdmin/page-error-400.html')


@login_required(login_url='login.html')
def import_file(request):
    if request.method == 'POST':
        customer_resource = ImportCustomerResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())

        print imported_data

        result = customer_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            customer_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'ElaAdmin/index.html')


@login_required(login_url='login.html')
def exportCustomer(request):

    data = Customer.objects.all()
    content = {
        'data': data
    }
    return render(request, 'ElaAdmin/exportCustomer.html', content)


@login_required(login_url='login.html')
def add_details_Customer(request):
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = AddCustomerDetailsForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            try:
                obj = Customer()
                obj.code = form.cleaned_data['code']
                obj.name = form.cleaned_data['name']
                obj.name = form.cleaned_data['name']
                obj.save()
            except IntegrityError:
                return HttpResponseRedirect('/page-error-400.html')

            return HttpResponseRedirect('/')
    else:
        form = AddCustomerDetailsForm()
        return render(request, 'ElaAdmin/addCustomer.html', {'form': form})


@login_required(login_url='login.html')
def add_details_Invoice(request):
    # customer_code = request.session.get('code')
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = AddInvoiceDetailsForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            objects = Customer.objects.all()
            for obj in objects:
                if obj.code == form.cleaned_data['code']:
                    # enter in the db
                    inv_obj = Invoice()
                    inv_obj.customer = obj
                    inv_obj.invoice_number = form.cleaned_data['invoice_number']
                    inv_obj.amount = form.cleaned_data['amount']
                    inv_obj.save()
                    # success message to be displayed

                    return HttpResponseRedirect('/index.html')

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # return HttpResponseRedirect('')

            return HttpResponseRedirect('/page-error-400.html')
    else:
        form = AddInvoiceDetailsForm()
        return render(request, 'ElaAdmin/addInvoice.html', {'form': form})
