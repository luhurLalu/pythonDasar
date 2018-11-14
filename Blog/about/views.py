from django.shortcuts import render
def index(request):
	context ={
	'title' : 'About',
	'heading' : 'Welcome to About Dashboard',
	'subheading' : 'This websites create using Django !',
	'image' : 'img/mainHeader.jpg',
	'css_app' : 'about/css/styles.css',
	}
	return render(request,'about/index.html',context)
# Create your views here.
