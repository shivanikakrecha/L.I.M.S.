# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_auto_20170914_1158'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Locations',
            new_name='Location',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Makes',
            new_name='Manufacture',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Technicians',
            new_name='Technician',
        ),
    ]