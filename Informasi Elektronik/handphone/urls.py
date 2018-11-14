from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'detail/(?P<slugInput>[\w-]+)',views.detail),
    url(r'kategori/(?P<merkInput>[\w-]+)',views.kategori),
]
