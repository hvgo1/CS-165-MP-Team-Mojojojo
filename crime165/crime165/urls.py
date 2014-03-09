from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crime165.views.home', name='home'),
    # url(r'^crime165/', include('crime165.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
      url(r'^crime/', include('crime.urls',namespace="crime")),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
