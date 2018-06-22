from django import forms
from Client.models import Client

class AddCustomerDetailsForm(forms.Form):
    code = forms.IntegerField(
        label='Customer Code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-number',
                'name': 'val-number',
                'placeholder': 'Enter the code id..'
            }
        )
    )
    name = forms.CharField(
        label='Customer Name',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-username',
                'name': 'val-username',
                'placeholder': 'Enter a username..'
            }
        )
    )
    number = forms.IntegerField(
        label='Number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'placeholder': 'Enter your number..'
            }
        )
    )
    address = forms.CharField(
        label='Address',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'placeholder': 'Enter your address'
            }
        )
    )
    client = forms.CharField(
        label='Client',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'placeholder': 'Enter client name'
            }
        )
    )


class AddInvoiceDetailsForm(forms.Form):
    code = forms.IntegerField(
        label='Customer Code',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-number',
                'name': 'val-number',
                'placeholder': 'Enter the code id..'
            }
        )
    )
    invoice_number = forms.IntegerField(
        label='Invoice Number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-number',
                'name': 'val-number',
                'placeholder': 'Enter invoice number..'
            }
        )
    )
    total_amount = forms.FloatField(
        label='Total Amount',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-currency',
                'name': 'val-currency',
                'placeholder': 'Enter amount..'
            }
        )
    )
    pending_amount = forms.FloatField(
        label='Pending Amount',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-currency',
                'name': 'val-currency',
                'placeholder': 'Enter pending amount..'
            }
        )
    )
    issue_date = forms.DateField(
        label='Issue Date',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-date',
                'name': 'val-date',
                'placeholder': 'YYYY-MM-DD'
            }
        )
    )
    number = forms.IntegerField(
        label='Number',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'placeholder': 'Enter your number..'
            }
        )
    )
    client = forms.CharField(
        label='Client',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'placeholder': 'Enter client name'
            }
        )
    )



