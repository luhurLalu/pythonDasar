from django.shortcuts import render
def index(request):
	context = {
	    'title' : 'Blog',
	    'heading' : 'Blog Dashboard',
	    'subheading' : 'This websites create using Django !',
	    'image' : 'img/mainHeader.jpg',
	    'css_app' : 'blog/css/styles.css',
	}	
	return render(request,'blog/index.html',context)
	