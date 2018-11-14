
from django.conf.urls import url, include
from django.contrib import admin
from authentication import views

 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #Login url
    url(r'^login/$', views.LoginView.as_view(),name='login'),
    url(r'^login/proses/$', views.ProsesLoginView.as_view(),name='proses_login'),
    url(r'^logout/$', views.LogoutProsesView.as_view(),name='logout'),
    #Read Url
    url(r'^home/$',views.HomeView.as_view(),name='home'),
    url(r'^course/',include('course.urls')),

    url(r'^course/', include('course.urls',namespace='course')), 
]
