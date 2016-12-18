from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^sinup/', 'sample1.views.sinup'),
url(r'^admin/', include(admin.site.urls)),
)
