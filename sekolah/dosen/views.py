from django.shortcuts import render

def index(request):
	context = {
		'css_app' : 'dosen/css/styles.css',
		'img' : 'dosen/img/dosen.jpg',
		'title' : 'Dosen',
		'head' : 'Dosen Dashboard',
		'sub' : [
			['/biodataDosen','Daftar Dosen'],
			['/listDosen','Daftar Dosen'],
		],
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		]
	}
	return render(request, 'index.html',context)

def listDosen(request):
	context = {
		'title' : 'Dosen | List',
		'head' : 'Daftar Dosen Dashboard',
		'sub' : [			
			['/listDosen','Daftar Dosen'],
			['/biodataDosen','Biodata Dosen'],
		],
		'nav' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		],
		'css_app' : 'dosen/css/styles.css',
		'img' : 'dosen/img/dosen.jpg',
	}
	return render(request,'dosen/index.html',context)

def biodataDosen(request):
	context = {
		'title' : 'Dosen | Biodata',
		'head' : 'Biodata Dosen Dashboard',
		'sub' : [
			['/listDosen','Daftar Dosen'],
			['/biodataDosen','Biodata Dosen'],
		],
		'nav' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		],
		'css_app' : 'dosen/css/styles.css',
		'img' : 'dosen/img/dosen.jpg',
	}
	return render(request, 'dosen/index.html',context)	
# Create your views here.
