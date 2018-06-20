# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-20 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField()),
                ('total_amount', models.FloatField()),
                ('pending_amount', models.FloatField()),
                ('number', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending', to='Customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('method', models.CharField(max_length=20)),
                ('details', models.CharField(max_length=300)),
                ('number', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Client')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.Customer')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.Profile')),
            ],
        ),
    ]
