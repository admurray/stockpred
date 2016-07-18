'''
Filename        : stocks.py                                            |  2
Author          : Aditya Murray                                        |  3 
Date            : 5th July 2016                                       |
Description     : set the index url
'''        

from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.index, name='index'),
        ]
