from django.db import models
from Client.models import Client, Profile
# Create your models here.


class Customer(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # is on_delete required?
    phone_no = models.CharField(max_length=10)
    address = models.CharField(max_length=200, null=True)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return str(self.code)


class Invoice(models.Model):

    customer = models.ForeignKey(Customer, related_name='invoice', on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    total_amount = models.FloatField()
    pending_amount = models.FloatField()
    number = models.CharField(max_length=20)  # char field
    issue_date = models.DateField()
    client = models.ForeignKey(Client)  # is on_delete required?

    def __str__(self):
        return str(self.invoice_number)


class Receipt(models.Model):

    profile = models.ForeignKey(Profile)
    customer = models.ForeignKey(Customer)
    client = models.ForeignKey(Client)
    amount = models.FloatField()
    issue_date = models.DateField()
    method = models.CharField(max_length=20)  # payment method
    details = models.CharField(max_length=300)  # extra details
    number = models.CharField(max_length=20)  # char field

    def __str__(self):
        return self.number