from django.shortcuts import render
from .models import Handphone

def index(request):
    context ={
        'title' : 'Handphone',
        'heading' : 'Informasi Handphone',
        'dataHp' : Handphone.objects.all(),
        'sortir' : Handphone.objects.values('merk').distinct(),          
    }
    return render(request,'handphone/index.html',context)

def detail(request, slugInput):
    context = {
        'title' : 'Detail',
        'heading' : 'Detail Handphone',
        'details' : Handphone.objects.get(slug=slugInput),  
        'sortir' : Handphone.objects.values('merk').distinct(),  
    }
    return render(request,'handphone/detail.html',context)

def kategori(request, merkInput):
    context = {
        'title' : 'Kategori',
        'heading' : 'Berdasarkan Kategori',
        'details' : Handphone.objects.filter(merk=merkInput),
        'sortir' : Handphone.objects.values('merk').distinct(),
        'dataHp' : Handphone.objects.all(),
    }
    return render(request,'handphone/category.html',context)
