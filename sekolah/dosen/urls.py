from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^listDosen/$',views.listDosen),
	url(r'^biodata/$',views.biodataDosen),
]