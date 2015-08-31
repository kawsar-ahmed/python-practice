from django.conf.urls import include, url
from polls.views import test
from django.contrib import admin

urlpatterns = [
	url(r'^hhh/', test),
]