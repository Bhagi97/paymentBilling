from django.shortcuts import render
from django.http import HttpResponseRedirect
from Customer.models import Customer, Invoice
from Customer.forms import *
from django.db import IntegrityError
from tablib import Dataset
from .forms import *

from Client.models import Profile, Client
from django.core.exceptions import ObjectDoesNotExist

from Customer.resources import ImportCustomerResource

from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.


def group_check_admin(user):
    return user.groups.filter(name__in=['admin', 'superuser', 'supervisor'])


def is_superuser(user):
    return user.groups.filter(name__in=['superuser']).exists()


def is_admin(user):
    return user.groups.filter(name__in=['admin']).exists()


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
                # for x in Permission.objects.filter(user=request.user):
                #     perm_list[x.codename] = True
                # context = {'permissions': perm_list}

                return HttpResponseRedirect('/index.html')
            else:
                # display not user page
                return HttpResponseRedirect('/page-error-403.html')

    else:
        form = LoginForm()
        return render(request, 'ElaAdmin/login.html', {'form': form})


# @login_required(login_url='login.html')
def logout_request(request):
    logout(request)
    form = LoginForm()
    return render(request, 'ElaAdmin/login.html', {'form': form})


@login_required
# @user_passes_test(is_superuser)
# @user_passes_test(is_admin)
def add_profile(request):

    if request.method == 'POST':
        # create form instance and populate it with data:
        form = RegisterProfileForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email_id = form.cleaned_data['email_id']

            newuser = User.objects.create_user(username, email_id, password)
            newuser.save()

            role_key = form.cleaned_data['role']
            roles = {
                '1': 'admin',
                '2': 'supervisor',
                '3': 'sales'
            }
            role = roles[role_key]

            phone_no = form.cleaned_data['phone_no']
            try:
                if request.user.groups.filter(name__in=['superuser']).exists():
                    client = Client.objects.get(name=form.cleaned_data['client'])  # if superuser
                elif request.user.groups.filter(name__in=['admin']):
                    # current_profile = Profile.objects.get(user=request.user)
                    client_name = request.user.profile.client.name
                    client = Client.objects.get(name=client_name)

            except ObjectDoesNotExist:
                return HttpResponseRedirect('/page-error-400.html')

            kwargs = {'user': newuser, 'role': role, 'client': client, 'phone_no': phone_no, }
            profile = Profile(**kwargs)
            profile.save()

            my_group = Group.objects.get(name=role)
            my_group.user_set.add(newuser)

            return HttpResponseRedirect('/index.html')

        else:
            return HttpResponseRedirect('<h1>Form invalid</h1>')

    else:
        form = RegisterProfileForm()
        return render(request, 'ElaAdmin/add_profile.html', {'form': form})


@login_required(login_url='login.html')
@user_passes_test(group_check_admin, login_url='../page-error-403.html')
# @user_passes_test(is_superuser, login_url='../page-error-403.html')
# @user_passes_test(is_admin, login_url='../page-error-403.html')
def index(request):

    return render(request, 'ElaAdmin/index.html')


def page_error_403(request):
    return render(request, 'ElaAdmin/page-error-403.html')


def page_error_400(request):
    return render(request, 'ElaAdmin/page-error-400.html')


# @login_required(login_url='login.html')
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


# @login_required(login_url='login.html')
def exportCustomer(request):

    data = Customer.objects.all()
    content = {
        'data': data
    }
    return render(request, 'ElaAdmin/exportCustomer.html', content)


# @login_required(login_url='login.html')
def add_details_Customer(request):
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = AddCustomerDetailsForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            try:
                code = form.cleaned_data['code']
                client_name = form.cleaned_data['client']
                name = form.cleaned_data['name']
                number = form.cleaned_data['number']
                address = form.cleaned_data['address']

                client = Client.objects.get(name=client_name)

                # clients = Client.objects.all()
                # client = clients[int(client_key)]

                kwargs = {'code': code, 'name': name, 'client': client, 'number': number, 'address': address,}
                customer = Customer(**kwargs)
                customer.save()

                return HttpResponseRedirect('/')


            except IntegrityError:
                return HttpResponseRedirect('/page-error-400.html')



    else:
        form = AddCustomerDetailsForm()
        return render(request, 'ElaAdmin/addCustomer.html', {'form': form})


# @login_required(login_url='login.html')
def add_details_Invoice(request):
    # customer_code = request.session.get('code')
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = AddInvoiceDetailsForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data

            code_no = form.cleaned_data['code']
            customer = Customer.objects.get(code=code_no)
            invoice_number = form.cleaned_data['invoice_number']
            total_amount = form.cleaned_data['total_amount']
            pending_amount = form.cleaned_data['pending_amount']
            issue_date = form.cleaned_data['issue_date']
            number = form.cleaned_data['number']
            client_name = form.cleaned_data['client']
            client = Client.objects.get(name=client_name)

            kwargs = {'customer': customer, 'client': client, 'invoice_number': invoice_number, 'total_amount': total_amount, 'pending_amount': pending_amount, 'issue_date': issue_date, 'number': number,}
            invoice = Invoice(**kwargs)
            invoice.save()

            return HttpResponseRedirect('/index.html')

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            # return HttpResponseRedirect('')

            # return HttpResponseRedirect('/page-error-400.html')
    else:
        form = AddInvoiceDetailsForm()
        return render(request, 'ElaAdmin/addInvoice.html', {'form': form})
