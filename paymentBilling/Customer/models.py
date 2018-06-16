from django.db import models

# Create your models here.


class Customer(models.Model):
    code = models.IntegerField(unique=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.code)


class Invoice(models.Model):
    customer = models.ForeignKey(Customer, related_name='pending', on_delete=models.CASCADE)
    invoice_number = models.IntegerField()
    amount = models.FloatField()
    pending = models.BooleanField(default=True)

    def __str__(self):
        return str(self.invoice_number)
