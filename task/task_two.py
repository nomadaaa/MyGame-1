dana = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
kendaraan_genap, kendaraan_ganjil = 0, 0
for i in list_plat_nomor:
	if i % 2 == 0:
		kendaraan_genap += i
	else:
		kendaraan_ganjil += i
	print('ganjil', kendaraan_ganjil)
	print(kendaraan_genap)

