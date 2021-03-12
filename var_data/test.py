sepatu = {
	"nama":"Sepatu Niko",
	"harga":150000,
	"diskon":300000
}
celana = {
	"nama":'Celana Lepis',
	'harga':200000,
	'diskon':230990
}
daftar_belanja = [sepatu, celana]

totalCelana = celana['harga'] - celana['diskon']
totalPajak = totalCelana * 0.1
print(totalPajak)

