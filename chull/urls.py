from django.conf.urls import include, url
from chull.views import index,xyz
from django.contrib import admin

urlpatterns = [
	url(r'^list/', index),
	url(r'^dict/$', xyz),
]