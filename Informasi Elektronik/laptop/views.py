from django.shortcuts import render
from.models import Laptop

def index(request):
    context = {
        'title' : 'Laptop',
        'heading' : 'Informasi Laptop',
        'all' : Laptop.objects.all(),
        'unik' : Laptop.objects.values('merk').distinct()
    }
    return render(request,'laptop/index.html',context)
 
def detail(request, slugInput):
    context = {
        'title' : 'Detail',
        'heading' : 'Detail Produk',        
        'slugs' : Laptop.objects.get(slug = slugInput),
        'unik' : Laptop.objects.values('merk').distinct()
    }
    return render(request,'laptop/detail.html',context)

def category(request,merkInput):
    context = {
        'title' : 'Kategori',
        'heading' : 'Kategori Berdasarkan Merk',        
        'saring' : Laptop.objects.filter(merk=merkInput), 
        'unik' : Laptop.objects.values('merk').distinct()
    }    
    return render(request,'laptop/category.html',context)