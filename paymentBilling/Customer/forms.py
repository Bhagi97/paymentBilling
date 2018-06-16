from django import forms


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
    amount = forms.FloatField(
        label='Amount',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-rounded',
                'id': 'val-currency',
                'name': 'val-currency',
                'placeholder': 'Enter amount..'
            }
        )
    )

