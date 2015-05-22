from django.conf.urls import patterns, include, url
from django.contrib import admin

from fundana.views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^index/$', index, name='index'),
    url(r'^about/$', about, name='about'),

    url(r'^hold/', include('app.hold.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('app.account.urls')),
)
