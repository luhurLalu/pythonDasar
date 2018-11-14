from django.conf.urls import url
 
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^alumni/$',views.alumni),
	url(r'^maba/$',views.maba),
]