# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-24 04:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=6, unique=True)),
                ('customer_name', models.CharField(max_length=50)),
                ('doctor_name', models.CharField(max_length=50)),
                ('request', models.CharField(max_length=100)),
                ('receptionist_name', models.CharField(max_length=30)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AuditReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(max_length=30)),
                ('bill', models.CharField(max_length=30)),
                ('no', models.IntegerField()),
                ('no_items', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('category_code', models.CharField(max_length=20)),
                ('category_description', models.CharField(max_length=200, null=True)),
                ('franchise_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('district_code', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phoneno', models.CharField(max_length=15)),
                ('phoneno_sec', models.CharField(max_length=15)),
                ('emailid', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('gstno', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateTimeField()),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('customer_code', models.CharField(max_length=10, unique=True)),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=25)),
                ('discount_type', models.CharField(max_length=10)),
                ('value', models.FloatField()),
                ('franchise_code', models.IntegerField(default=0)),
                ('franchise_name', models.CharField(default='Head Office', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10, null=True)),
                ('sid', models.IntegerField(default=None, null=True)),
                ('pid', models.IntegerField(default=None, null=True)),
                ('trid', models.IntegerField(default=None, null=True)),
                ('tid', models.CharField(max_length=10)),
                ('requested_time', models.DateTimeField(default=None, null=True)),
                ('franchise_code', models.IntegerField(null=True)),
                ('status', models.CharField(default='Pending', max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('confirmed_time', models.DateTimeField(default=None, null=True)),
                ('lastchanged', models.DateTimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Franchise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_name', models.CharField(max_length=100, unique=True)),
                ('franchise_type', models.CharField(max_length=10)),
                ('phoneno', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('town', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=50)),
                ('bankaccountno', models.CharField(max_length=50)),
                ('bankname', models.CharField(max_length=50)),
                ('ifsccode', models.CharField(max_length=20)),
                ('gstno', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=10)),
                ('owner', models.CharField(max_length=20)),
                ('ownercontact', models.CharField(max_length=10)),
                ('remarks', models.CharField(max_length=300, null=True)),
                ('permbs1', models.BooleanField()),
                ('permbs2', models.BooleanField()),
                ('currency', models.CharField(max_length=10)),
                ('permb3', models.BooleanField()),
                ('permb4', models.BooleanField()),
                ('permb5', models.BooleanField()),
                ('active', models.BooleanField(default=True)),
                ('sales_today', models.FloatField(default=0)),
                ('customers_today', models.FloatField(default=0)),
                ('new_customers', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HOProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('MRP', models.FloatField(null=True)),
                ('SKU', models.CharField(max_length=15)),
                ('stock', models.IntegerField(default=0)),
                ('tax_CGST', models.FloatField(default=0)),
                ('tax_SGST', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Implementation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_code', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('date_mou', models.DateField()),
                ('painting', models.BooleanField()),
                ('electrification', models.BooleanField()),
                ('signboard', models.BooleanField()),
                ('installation_of_required_equipment', models.BooleanField()),
                ('inaugration_date', models.DateField()),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('franchise_code', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('v1', models.CharField(max_length=10)),
                ('v2', models.CharField(max_length=10)),
                ('v3', models.CharField(max_length=10)),
                ('v4', models.CharField(max_length=10)),
                ('v5', models.CharField(max_length=10)),
                ('v6', models.CharField(max_length=10)),
                ('v7', models.CharField(max_length=10)),
                ('staff_behaviour', models.CharField(max_length=10)),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pic', models.ImageField(upload_to=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
                ('package_code', models.CharField(max_length=20, unique=True)),
                ('rates', models.CharField(max_length=30)),
                ('body_part', models.CharField(max_length=30, null=True)),
                ('tax_CGST', models.FloatField(null=True)),
                ('tax_SGST', models.FloatField(null=True)),
                ('remarks', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PackageMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask', models.CharField(max_length=500)),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PendingPrescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=6)),
                ('customer_name', models.CharField(max_length=50)),
                ('doctor_name', models.CharField(max_length=30)),
                ('franchise_code', models.IntegerField()),
                ('consultation_fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PendingTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=6)),
                ('customer_name', models.CharField(max_length=50)),
                ('doctor_name', models.CharField(max_length=30)),
                ('franchise_code', models.IntegerField()),
                ('consultation_fees', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pending_prescription', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PendingPrescription')),
                ('pending_treatment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PendingTreatment')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('short_code', models.CharField(max_length=10)),
                ('MRP', models.IntegerField(null=True)),
                ('SKU', models.CharField(max_length=15)),
                ('tax_CGST', models.FloatField(default=0)),
                ('tax_SGST', models.FloatField(default=0)),
                ('category', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=200)),
                ('franchise_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=50)),
                ('regid', models.CharField(default='0', max_length=30)),
                ('organisation', models.CharField(max_length=100)),
                ('franchise_code', models.IntegerField(default=0)),
                ('phoneno', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('itemwise_discount', 'Can set discount - Granularity:Item'), ('categorywise_discount', 'Can set discount - Granularity:Category'), ('price_discount', 'Can set price wise discount'), ('percentage_discount', 'Can set percentage wise discount'), ('viewdoctor', 'Can view doctor details'), ('viewpatient', 'Can view patient details'), ('prescribe', 'Can prescribe medicine'), ('addbill', 'Can add bill'), ('viewbill', 'Can edit bill'), ('adduser', 'Can add user'), ('modifyuser', 'Can modify user'), ('distributor', 'Is a distributor'), ('ho', 'Is a Head Office Member'), ('prescriptionreport', 'Can see Prescription Report')),
            },
        ),
        migrations.CreateModel(
            name='SalesReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=80)),
                ('quantity', models.IntegerField()),
                ('sale_rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesReportBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('bill_type', models.CharField(max_length=30)),
                ('franchise_code', models.IntegerField()),
                ('customer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='SavedBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=10)),
                ('franchise_code', models.IntegerField()),
                ('productlist', models.CharField(max_length=200)),
                ('ratelist', models.CharField(max_length=200)),
                ('durationlist', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='scans')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('service_code', models.CharField(max_length=20, unique=True)),
                ('rates', models.CharField(max_length=30)),
                ('body_part', models.CharField(max_length=30, null=True)),
                ('tax_CGST', models.FloatField(null=True)),
                ('tax_SGST', models.FloatField(null=True)),
                ('remarks', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to=b'')),
                ('duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mask', models.CharField(max_length=500)),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SKUList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('unit', models.CharField(max_length=30)),
                ('franchise_code', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('stock_quantity', models.IntegerField()),
                ('franchise_code', models.IntegerField()),
                ('batch_no', models.CharField(max_length=20)),
                ('vendor', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('gst_no', models.CharField(max_length=30)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StockReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=30)),
                ('item_name', models.CharField(max_length=30)),
                ('stock', models.IntegerField()),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StockTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=30)),
                ('stock_amount', models.CharField(max_length=20)),
                ('franchise_name', models.CharField(max_length=30)),
                ('discount', models.IntegerField(null=True)),
                ('expiry_date', models.DateField()),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimestampDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rate', models.FloatField()),
                ('tax_CGST', models.FloatField(null=True)),
                ('tax_SGST', models.FloatField(null=True)),
                ('franchise_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('remarks', models.CharField(max_length=200)),
                ('duration', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='salesreport',
            name='sales_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.SalesReportBase'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('item_name', 'franchise_code')]),
        ),
        migrations.AddField(
            model_name='inspection',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='implementation',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
        migrations.AddField(
            model_name='franchise',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adminmap', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='franchise',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributormap', to='app.Profile'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='p',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Package'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='s',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Service'),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='t',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.TreatmentMaster'),
        ),
        migrations.AddField(
            model_name='discount',
            name='pid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Package'),
        ),
        migrations.AddField(
            model_name='discount',
            name='proid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
        migrations.AddField(
            model_name='discount',
            name='sid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Service'),
        ),
        migrations.AddField(
            model_name='discount',
            name='tid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Treatment'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('category_name', 'franchise_code')]),
        ),
        migrations.AddField(
            model_name='appointment',
            name='franchise',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Franchise'),
        ),
    ]
