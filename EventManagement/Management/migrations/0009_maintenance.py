# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0008_issueproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Action', models.CharField(choices=[('replace', 'replace'), ('Maintain', 'Maintain'), ('Repair', 'Repair'), ('Garbage', 'Garbage')], default='', max_length=100)),
                ('Post', models.TextField(default='', max_length=250)),
                ('maintain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Management.IssueProduct')),
            ],
        ),
    ]