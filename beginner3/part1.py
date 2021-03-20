
#* membuat class karyawan yang akan berfungsi sebagai blueprint
#* class biasanya menggunakan huruf kapital pada awal hurufnya
#* di dalam class mempunyai atribut dan properti
class Karyawan:
	#* salah satu penggunaan class attribut
	nama_perusahaan = 'ABC'
	#* didalam sebuah class biasanya terdapat sebuah constructor
	#* constructor di python disebut __init__()
	#* fungsi cons yaitu kita bisa menginisialisasi attribut milik objek
	#* contoh
	#* self ialah parameter pertama yang dibawa oleh semua function
	#* kemudian dilanjutkan dengan parameter2 yg lain
	def __init__(self, nama, umur, gaji):
		self.nama = nama
		self.gaji = gaji
		self.umur = umur

	# pass

#* ini merupakan contoh objek dari class karyawan
agum = Karyawan('Agum', 20, 10000000)
senja = Karyawan()


#* mengubah isi dari attribut class
agum.__class__.nama_perusahaan = 'DEF'
#* mengakases attribut dari class
print('agum', agum.__class__.nama_perusahaan)
print('senja', senja.__class__.nama_perusahaan)