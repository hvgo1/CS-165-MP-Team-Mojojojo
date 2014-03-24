from django.conf.urls import patterns, url

from crime import views

urlpatterns = patterns('',
    #url(r'^$', views.index, name='index'),
    url(r'^viewcrimes', views.CrimeView.as_view(), name='viewcrimes'),
 #   url(r'^updatecrimes', views.CrimeUpdate.as_view(), name='updatecrimes'),
    url(r'^addcategory', views.addCategory, name='addcategory'),
    url(r'^addagent', views.addAgent, name='addagent'),
    url(r'^addlocation', views.addLocation, name='addlocation'),
    url(r'^addcrime', views.addCrime, name='addcrime'),
    url(r'^addsuspect', views.addSuspect, name='addsuspect'),
#    url(r'^index.html', views.index, name='index'),
    
    )
