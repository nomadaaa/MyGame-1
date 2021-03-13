dana = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
kendaraan_genap = 0
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
	if plat_nomor % 2 == 0:
		kendaraan_genap += 1
	else:
		kendaraan_ganjil += 1

i = 0
total_pengeluaran = 0
while i <= jumlah_hari:
	if i % 2 == 0:
		total_pengeluaran += (kendaraan_genap * dana)
	else:
		total_pengeluaran += (kendaraan_ganjil * dana)

i += 1
print(total_pengeluaran)

