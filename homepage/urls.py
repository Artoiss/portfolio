from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^cv/$', views.cv),
    url(r'^contact/$', views.contact)
]
