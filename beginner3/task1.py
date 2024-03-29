

#* membuat class
class Karyawan:
	insentif_proyek = 0

	#* func init
	def __init__(self, nama, usia, pendapatan, insentif_lembur=0):
		self.nama = nama
		self.usia = usia
		self.pendapatan = pendapatan
		self.insentif_lembur = insentif_lembur
		self.point = 0
		self.bonus = 0

	#* membuat fungsi lembur
	#* kita check berapa jam pegawai lembur
	def lembur(self, jam=0):
			#* membuat variabel jam
			#* menghitung berapa lama pegawai lembur
			#* > 6 == 500
			#* 250
		self.jam = jam
		if jam >= 6:
			self.insentif_lembur += 500000
		else:
			self.insentif_lembur += 250000
		
		self.bonus += self.insentif_lembur

	#* func proyek
	#* proyek dihitung berdasarkan point
	#* 1 proyek = 2.5 point
	#* 10 point = 1000000
	def proyek(self, jumlah):
		self.jumlah = jumlah
		self.point = 2.5 * jumlah

		if self.point == 10:
			self.insentif_proyek = 1000000

		#* bonus + insentif proyek
		self.bonus += self.insentif_proyek		


	#* func total
	#* menambah insentif lembur dan pendapatan 
	def total_pendapatan(self):
		return self.pendapatan + self.bonus

#* execute program
pegawai1 = Karyawan('Agum', 22, 3000000)
pegawai1.lembur(2)
pegawai1.proyek(4)
print(pegawai1.total_pendapatan())
# print(pegawai1.proyek(3))

#* membuat class perusahaan 
#* berisi nama, alamat, nomor_tlp
class Perusahaan:
	def __init__(self, nama, alamat, nomot_tlp):
		self.nama = nama
		self.alamat = alamat
		self.nomor_tlp = nomot_tlp
		self.list_karyawan = []

	def karyawan(self, status):
		self.nama 
		self.status = status
	
	def aktifkan_karyawan(self, karyawan):
		self.list_karyawan.append(karyawan)

	def nonaktifkan_karyawan(self, nama_karyawan):
		karyawan_nonaktif = None
		for karyawan in self.list_karyawan:
			if karyawan.nama == nama_karyawan:
				karyawan_nonaktif = karyawan
				break
			if karyawan.nama is not None:
				self.list_karyawan.remove(karyawan_nonaktif)
	

perusahaan1 = Perusahaan('Unilever', 'Jakarta', '02141158')
print(perusahaan1.aktifkan_karyawan('karyawan'))
print(perusahaan1.nama)

#* deklarasi objek perusahaan dan karyawan
nama_perusahaan = Perusahaan('Compus Tech', 'Jakarta', '021111221')
ani = Karyawan('Ani', 22, 200234244)
ani.lembur(6)
ani.proyek(4)
print(ani.total_pendapatan())


