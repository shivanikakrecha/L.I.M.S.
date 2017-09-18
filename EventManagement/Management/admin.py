# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . models import Enventory, Product, IssueProduct, Maintenance
from django.contrib import admin

# Register your models here.
admin.site.register(Enventory)
admin.site.register(Product)
admin.site.register(IssueProduct)
admin.site.register(Maintenance)