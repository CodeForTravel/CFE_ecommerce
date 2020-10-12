
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

from .views import register

urlpatterns = [


    url(r'^login/$', login,{'template_name' : 'login.html'}, name='login'),
    url(r'^register/$', views.register, name ='signup')
]
