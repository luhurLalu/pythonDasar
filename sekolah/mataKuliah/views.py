from django.shortcuts import render

def index(request):
	context = {
		'title' : 'Matakuliah ',
		'head' : 'Mata Kuliah Dashboard',
		'sub' : [
			['/mataKuliah/prasyarat','Mata Kuliah Prasyarat'],
			['/mataKuliah/teori','Mata Kuliah Teori'],
		],
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		],
		'css_app' : 'mataKuliah/css/styles.css',
		'img' : 'mataKuliah/img/sekolah.png'
	}
	return render(request, 'index.html',context)

def prasyarat(request):
	context = {
		'title' : 'Matakuliah | Prasyarat',
		'head' : 'Daftar Mata Kuliah Prasyarat',
		'sub' : [
			['/mataKuliah/prasyarat','Mata Kuliah Prasyarat'],
			['/mataKuliah/teori','Mata Kuliah Teori'],
		],
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		],		
		'css_app' : 'mataKuliah/css/styles.css',
		'img' : 'mataKuliah/img/sekolah.png'
	}
	return render(request, 'index.html',context)

def teori(request):
	context = {
		'title' : 'Matakuliah | Teori',
		'head' : 'Daftar Mata Kuliah Teori',
		'sub' : [
			['/mataKuliah/prasyarat','Mata Kuliah Prasyarat'],
			['/mataKuliah/teori','Mata Kuliah Teori'],
		],
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		],		
		'css_app' : 'mataKuliah/css/styles.css',
		'img' : 'mataKuliah/img/sekolah.png'
	}
	return render(request, 'index.html',context)
# Create your views here.
