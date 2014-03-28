from django.conf.urls import patterns, url

from crime import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^crimelist', views.CrimeList, name ='crimelist'), 
    url(r'^updatecrime/(?P<id>\d+)', views.updateCrime, name ='updatecrime'),
    url(r'^deletecrime/(?P<id>\d+)', views.deleteCrime, name ='updatecrime'),
    url(r'^updatecrime/crimelist', views.CrimeList, name ='crimelist'),
    url(r'^deletecrime/crimelist', views.CrimeList, name ='crimelist'),
    url(r'^viewcrime/(?P<id>\d+)', views.viewCrime, name='viewcrime'),
    url(r'^suspectlist', views.SuspectList, name ='suspectlist'), 
    url(r'^updatesuspect/(?P<id>\d+)', views.updateSuspect, name ='updatesuspect'),
    url(r'^deletesuspect/(?P<id>\d+)', views.deleteSuspect, name ='updatesuspect'),
    url(r'^updatesuspect/suspectlist', views.SuspectList, name ='suspectlist'),
    url(r'^deletesuspect/suspectlist', views.SuspectList, name ='suspectlist'),
    url(r'^viewsuspect/(?P<id>\d+)', views.viewSuspect, name='viewsuspect'),
    url(r'^addcategory', views.addCategory, name='addcategory'),
    url(r'^addagent', views.addAgent, name='addagent'),
    url(r'^addlocation', views.addLocation, name='addlocation'),
    url(r'^addcrime', views.addCrime, name='addcrime'),
    url(r'^addsuspect', views.addSuspect, name='addsuspect'),
   
    )
