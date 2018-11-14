from django.shortcuts import render

def index(request):
	context = {
		'img' : 'img/generic.jpg',
		'title' : 'Home | Sekolah',
		'head' : 'Sekolah Dashboard',
		'var' : [
			['/','Home'],
			['/mahasiswa','Mahasiswa'],
			['/dosen','Dosen'],
			['/mataKuliah','Mata Kuliah'],
		]
	}
	return render(request,'index.html',context)