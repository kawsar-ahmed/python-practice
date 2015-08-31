from django.conf.urls import include, url
from django.contrib import admin
from firstapp import views

urlpatterns = [
    url(r'^list/', views.list),
    url(r'^dict/$', views.dict),
    url(r'^input_info/$', views.input_info),
]