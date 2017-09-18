#tutorial 14
from django.shortcuts import redirect

def login_redirect(request):
    return redirect('/Management/login')

