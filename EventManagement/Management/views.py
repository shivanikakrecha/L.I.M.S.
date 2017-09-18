# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . forms import EnventoryForm, AddProductForm
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm
from Management.forms import (
    RegistrationForm,
    EnventoryForm,
    AddProductForm,
    IssueForm,
    MaintenanceForm
)

# Create your views here.
#def home(request):
 #   name = 'python'

   #return HttpResponse('home page!')
#    return render(request, 'Management/home.html')

def Home(request):
    return render(request, 'Management/home.html')

def home(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = EnventoryForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submited successfully')
            return redirect(reverse('Management:Home'))

    else:
        f = EnventoryForm()

    return render(request, 'Management/Enventory.html', {'form': f})



def register(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = RegistrationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submited successfully')
            return redirect(reverse('Management:login'))

    else:
        f = RegistrationForm()

    return render(request, 'Management/reg_form.html', {'form': f})


def AddProduct(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = AddProductForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submited successfully')
            return redirect(reverse('Management:AddProduct'))

    else:
        f = AddProductForm()

    return render(request, 'Management/AddProduct.html', {'form': f})


def IssueProduct(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = IssueForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submited successfully')
            return redirect(reverse('Management:IssueProduct'))

    else:
        f = IssueForm()

    return render(request, 'Management/IssueProduct.html', {'form': f})

def Maintenance(request):
    if request.method == 'POST':
        #f = UserCreationForm(request.POST)
        f = MaintenanceForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Submited successfully')
            return redirect(reverse('Management:Maintenance'))

    else:
        f = MaintenanceForm()

    return render(request, 'Management/Maintain.html', {'form': f})






