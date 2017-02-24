from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^plot/$', views.weather_chart_view),
]
