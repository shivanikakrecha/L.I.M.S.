from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^home/$', views.Home, name='Home'),
    url(r'^$', views.Home, name='home'),
    url(r'^login/$', login, {'template_name': 'Management/login.html'}, name='login'),

    url(r'^logout/$', logout, {'template_name': 'Management/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^enventory/$', views.home, name='Enventory'),
    url(r'^product/$', views.AddProduct, name='AddProduct'),
    url(r'^issue/$', views.IssueProduct, name='IssueProduct'),
    url(r'^maintain/$', views.Maintenance, name='Maintenance')

]