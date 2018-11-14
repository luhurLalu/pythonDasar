from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Berbasis fungsi dan class
class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request,self.template_name) 

class HomeView(View):
    template_name = 'home.html'
    def get(self, request):
        return render(request,self.template_name)

class ProsesLoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password ) 
        if user:
            login(request, user)            
            return redirect('/home')               
        messages.warning(request, 'Username or Password Incorrect !')         
        return redirect('/login/')

class LogoutProsesView(View):
    def get(self, request):
        if request.user.is_authenticated():
            logout(request)
            return redirect('login')
    

