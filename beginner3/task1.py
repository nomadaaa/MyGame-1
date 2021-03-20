

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
		self.bonus += self.insentif_proyek

	#* func total
	#* menambah insentif lembur dan pendapatan 
	def total_pendapatan(self):
		return self.pendapatan + self.bonus

#* execute program
pegawai1 = Karyawan('Agum', 22, 3000000)
pegawai1.lembur(6)
pegawai1.proyek(2)
# pegawai1.total_pendapatan()
print(pegawai1.total_pendapatan())