from django.conf.urls import patterns, include, url

urlpatterns = patterns('',  # NOQA
    url(r'', include('files.urls')),
)
