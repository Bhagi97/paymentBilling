from django import forms
from django.forms import ModelForm
from models import *


class StockTransferForm(forms.Form):
    class StockTransferForm(ModelForm):
        class Meta:
            model = StockTransfer
            fields = ['item_name', 'stock_amount', 'franchise_name' ,'discount','expiry_date']


class EditProfile(forms.Form):
    username = forms.CharField(max_length=50)
    company_name = forms.FileField()
    logo = forms.FileField()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)



