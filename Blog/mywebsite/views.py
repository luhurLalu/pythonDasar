from django.shortcuts import render

context = {
    'title' : 'Home',
    'heading' : 'Welcome to Home Dashboard',
    'subheading' : 'This websites create using Django !',    
}
def index(request):
    return render(request,'index.html',context)