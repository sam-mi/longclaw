# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-11 17:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('longclawshipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingcountry',
            options={'verbose_name_plural': 'shipping countries'},
        ),
    ]