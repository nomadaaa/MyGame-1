
#* membuat class karyawan yang akan berfungsi sebagai blueprint
#* class biasanya menggunakan huruf kapital pada awal hurufnya
#* di dalam class mempunyai atribut dan properti
class Karyawan:
	#* salah satu penggunaan class attribut
	nama_perusahaan = 'ABC'
	insentif_lembur = 1500000

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
		self.pendapatan_tambahan = 0
		#* mengecek umur 
		#* jika umur lebih dari 30 maka ditambah 1500000
		if umur > 30:
			self.gaji += 1500000

	#* didalam class kita juga bisa menambahkan fungsi
	#* contoh
	#* fungsi lembur
	def lembur(self):
		self.pendapatan_tambahan += self.insentif_lembur

	# pass

#* ini merupakan contoh objek dari class karyawan
agum = Karyawan('Agum', 20, 10000000)
senja = Karyawan('Senja', 35, 2100000)

#* mengakses objek 
print(agum.nama + ' pendapatan ' + str(agum.gaji) + ' Usia ' + str(agum.umur))
print(senja.nama + ' pendapatan ' + str(senja.gaji) + ' Usia ' + str(senja.umur))

#* mengubah isi dari attribut class
agum.__class__.nama_perusahaan = 'DEF'
#* mengakases attribut dari class
print('agum', agum.__class__.nama_perusahaan)
print('senja', senja.__class__.nama_perusahaan)