from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'goofy.views.home', name='home'),
    # url(r'^goofy/', include('goofy.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
