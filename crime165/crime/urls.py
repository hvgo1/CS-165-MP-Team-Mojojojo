from django.conf.urls import patterns, url

from crime import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^addCategory', views.addCategory, name='addCategory'),
    )
