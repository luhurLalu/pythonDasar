from django.shortcuts import render

def index(request):
	context = {
		'css_app' : 'mahasiswa/css/styles.css',
		'img' : 'mahasiswa/img/mahasiswa.jpg',
		'title' : 'Mahasiswa',
		'head' : 'Mahasiswa Dashboard',
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		]
	}
	return render(request,'index.html',context)

def alumni(request):
	context = {
		'title' : 'Mahasiswa | Alumni',
		'head' : 'Daftar Alumni Mahasiswa',
		'nav' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		]
	}
	return render(request,'mahasiswa/index.html',context)

def maba(request):
	context = {
		'title' : 'Mahasiswa | Baru',
		'head' : 'Daftar Mahasiswa Baru',
		'nav' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		]
	}
	return render(request,'mahasiswa/index.html',context)	
# Create your views here.
