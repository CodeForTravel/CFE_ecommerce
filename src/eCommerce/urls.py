"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import TemplateView

#from products.views import (
    #ProductListView,
    #product_list_view,
    #ProductDetailView,
    #product_detail_view,
    #ProductFeaturedDetailView,
    #ProductFeaturedListView,
    #ProductDetailSlugView
   # )

from .views import home_page, about_page

urlpatterns = [

    url(r'^$', home_page, name='home'),
    url(r'^about/$', about_page,name='about'),
    #url(r'^contact/$', contact_page, name='contact'),
    url(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/example.html')),
    #url(r'^login/$', login,{'template_name' : 'mainapp/login.html'} ),
    #url(r'^logout/$', logout,{'template_name' : 'mainapp/logout.html'} ),
    #url(r'^register/$', views.register, name ='register')

    #url(r'^product-fbv/$', product_list_view),
    #url(r'^featured/$', ProductFeaturedListView.as_view()),
    #url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    #url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    #url(r'^product-fbv/(?P<pk>\d+)/$',product_detail_view),
    #url(r'^product/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^products/', include('products.urls', namespace="products")),
    url(r'^cart/', include('carts.urls', namespace="cart")),
    url(r'^search/', include('search.urls', namespace="search")),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
