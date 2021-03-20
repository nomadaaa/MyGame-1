
#* membuat class karyawan yang akan berfungsi sebagai blueprint
#* class biasanya menggunakan huruf kapital pada awal hurufnya
#* di dalam class mempunyai atribut dan properti
class Karyawan:
	#* salah satu penggunaan class attribut
	nama_perusahaan = 'ABC'
	# pass

#* ini merupakan contoh objek dari class karyawan
agum = Karyawan()
senja = Karyawan()


#* mengubah isi dari attribut class
agum.__class__.nama_perusahaan = 'DEF'
#* mengakases attribut dari class
print(agum.__class__.nama_perusahaan)