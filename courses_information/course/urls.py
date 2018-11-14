
from django.conf.urls import url
from .views import CourseListView, CourseAddView, CourseDeleteView

urlpatterns = [
        
    url(r'^list/$', CourseListView.as_view(),name='list'),
    url(r'^add/$',CourseAddView.as_view(),name='add'),    
    url(r"^delete/(?P<course_id>\d+)/$",CourseDeleteView.as_view(),name='delete'),
]
