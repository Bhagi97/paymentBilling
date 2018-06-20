from django.contrib import admin
from .models import Customer, Invoice, Receipt
# Register your models here.
from import_export.admin import ImportExportModelAdmin


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    pass


# admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(Receipt)