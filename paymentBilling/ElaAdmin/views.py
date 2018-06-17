from django.shortcuts import render
from django.http import HttpResponseRedirect
from Customer.models import Customer, Invoice
from Customer.forms import *
# Create your views here.


def index(request):
    return render(request, 'ElaAdmin/index.html')


def page_error(request):
    return render(request, 'ElaAdmin/page-error-400.html')


def exportCustomer(request):
    return render(request, 'ElaAdmin/exportCustomer.html')


def add_details_Customer(request):
    if request.method == 'POST':
        # create form instance and populate it with data:
        form = AddCustomerDetailsForm(request.POST)

        # check if valid
        if form.is_valid():
            # process data
            obj = Customer()
            obj.code = form.cleaned_data['code']
            obj.name = form.cleaned_data['name']
            obj.save()
            # success message to be displayed

            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect('/')
    else:
        form = AddCustomerDetailsForm()
        return render(request, 'ElaAdmin/addCustomer.html', {'form': form})


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
