from models import *

def my_scheduled_job():
    fs = Franchise.objects.all()
    for f in fs:
        f.sales_today = 0
        f.customers_today = 0
        f.new_customers = 0
        f.save()

    Stock.objects.filter(stock_quantity=0).delete()


def my_scheduled_yearly_job():
    IDGenerator.objects.all().update(counter=0)
