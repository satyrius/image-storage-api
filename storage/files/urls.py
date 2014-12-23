from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',  # NOQA
    url(r'^upload/?$', views.upload),
)
