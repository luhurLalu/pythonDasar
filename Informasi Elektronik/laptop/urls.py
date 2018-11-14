from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'detail/(?P<slugInput>[\w-]+)',views.detail,name='showD'),
    url(r'category/(?P<merkInput>[\w-]+)',views.category,name='showC'),
]
 