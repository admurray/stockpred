'''
Filename        : stocks.py
Author          : Aditya Murray
Date            : 5th July 2016
Description     : Valid recognized urls
'''

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stockit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^stock_data/', include('stock_data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
