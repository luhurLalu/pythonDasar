from django.shortcuts import render

def index(request):
    context ={
        'title' : 'Home | Toko',
        'heading' : 'Selamat datang di Informasi Spesifikasi Elektronik'
    }
    return render(request,'index.html',context)