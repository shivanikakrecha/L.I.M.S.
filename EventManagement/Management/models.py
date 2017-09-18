# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from multiselectfield import MultiSelectField
from django.db import models
from datetime import tzinfo, timedelta, datetime, date

Product_choice = (
    ('Monitor', 'Monitor'),
    ('Laptop', 'Laptop'),
    ('Switch', 'Switch'),
    ('cable', 'Cable'),
    ('Key-board', 'Key-board')
)
# product_type = models.CharField(max_length=100, choices=Product_choice)

Manufactures = (
    ('HP', 'HP'),
    ('Sisco', 'Sisco'),
    ('Dell', 'Dell')
)

Use_to = (
    ('Employee', 'Employee'),
    ('Customer', 'Customer'),
    ('Technician', 'Technician'),
    ('Company', 'Company')
)

action = (
    ('replace','replace'),
    ('Maintain','Maintain'),
    ('Repair','Repair'),
    ('Garbage','Garbage')
)

location_list = (
    ('merit','merit'),
    ('lintel','lintel'),
    ('branch','branch')
)
# Create your models here.
class Enventory(models.Model):

    Product_Type = models.CharField(max_length=100, choices=Product_choice, default='')
    Manufacture = models.CharField(max_length=100, choices=Manufactures, default='')
    Serial_no = models.CharField(max_length=50, default='')
    Mac_ID = models.IntegerField(default='')
    Assigned_to = models.CharField(max_length=100, choices=Use_to, default='')
    Technician = models.CharField(max_length=100, default='')
    Purchase_date = models.CharField(max_length=100, default='')
    Issue_date = models.CharField(max_length=100, default='')
    Warntee = models.CharField(max_length=100, default='')
    Maintainance = models.CharField(max_length=100, default='')
    Location = models.CharField(max_length=50, default='')
    Comments = models.TextField(max_length=500, default='')
    Status = models.CharField(max_length=100, default='')
    Duration = models.CharField(max_length=100, default='')

class Product(models.Model):

    Products = models.CharField(max_length=100, choices=Product_choice, default='')
    Manufacture = models.CharField(max_length=100, choices=Manufactures, default='')
    Serial_nu = models.CharField(max_length=50, default='')
    Mac_Id = models.IntegerField(default='')
    Technician = models.CharField(max_length=100, default='')
    Assigned_To = models.CharField(max_length=100, choices=Use_to, default='')
    Purchase_Date = models.CharField(max_length=50, default='')
    Warranty_Time = models.CharField(max_length=50, default='')
    Location = models.CharField(max_length=50, choices=location_list, default='')

    def __str__(self):
        return self.Serial_nu


class IssueProduct(models.Model):

    products = models.ForeignKey(Product)
    known_issue = models.CharField(max_length=100, default='')
    status = models.CharField(max_length=100, default='')
    comments = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.known_issue

class Maintenance(models.Model):

    maintain = models.ForeignKey(IssueProduct)
    Action = models.CharField(max_length=100, choices=action, default='')
    Post = models.TextField(max_length=250, default='')

    def __str__(self):
        return self.Action



















