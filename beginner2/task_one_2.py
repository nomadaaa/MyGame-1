bulan = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni',
'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember'
)

#penggunaan list
pertengahan_tahun = bulan[4:9]
awal_tahun = bulan[:5]
akhir_tahun = bulan[8:]
print(pertengahan_tahun)
print('awal tahun', awal_tahun)
print('akhir tahun', akhir_tahun)
print(bulan[-4:-1])

#!penggabungan dua list atau lebih
list_makanan = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_minuman = ['Es Teh', 'Es Jeruk', 'Es Campur']
list_menu = list_makanan + list_minuman
print(list_menu)

#!fitur append
list_makanan.append('ketoprak')

#!clear
list_makanan.clear()

#!copy
list_makanan1 = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_makanan2 = list_makanan1.copy()
list_makanan3 = list_makanan1
print(list_makanan1, list_makanan2, list_makanan3)

#!count
score = ['Budi', 'Sud','Budi', 'Sud']
list_count = score.count('Budi')
print(list_count)