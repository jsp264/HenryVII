# urls.py for tudor

from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'tudor'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^toot(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^seek(?P<pk>[0-9]+)/$', views.DetailSeekView.as_view(), name='detail_seek'),
    url(r'^tutor_upload$', views.tutor_upload, name='tutor_upload'),
    url(r'^seek_upload$', views.seek_upload, name='seek_upload'),
] 