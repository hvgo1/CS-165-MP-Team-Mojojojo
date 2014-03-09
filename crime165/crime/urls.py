from django.conf.urls import patterns, url

from crime import views

urlpatterns = patterns('',
   # url(r'^$', views.IndexView.as_view(), name='index'),
   # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<pk>\d+)/results/$', #views.ResultsView.as_view(), name='results'),
   # url(r'^(?P<crime_id>\d+)/addCategory/$', views.addCategory, name='addCategory'),
    url(r'^$', views.index, name='index'),
    url(r'^addCategory', views.addCategory, name='addCategory'),
    )
