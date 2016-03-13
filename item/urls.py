from django.conf.urls import patterns, url
from item import views



urlpatterns = patterns('',
    url(r'^items/$', views.item_list, name='item_list'),
    
    )

