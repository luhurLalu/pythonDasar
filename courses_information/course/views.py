from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course
 
class CourseListView(View):
    template_name =  'course_list.html'

    def get(self, request):
        data = {

            'courses' : Course.objects.all()
        }
        return render(request, self.template_name, data)

class CourseAddView(View):
    template_name = 'add_list.html'

    def get(self, request):
        return render(request, self.template_name)

class CourseDeleteView(View):
    def get(self, request, course_id):
        obj = Course.objects.get(id=course_id)
        obj.delete()
                                    
        messages.warning(request, 'Delete succes !')
        return redirect('course:list')
            

# Create your views here.
