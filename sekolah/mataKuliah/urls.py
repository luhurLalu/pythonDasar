from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^prasyarat/$',views.prasyarat),
	url(r'^teori$',views.teori),
]