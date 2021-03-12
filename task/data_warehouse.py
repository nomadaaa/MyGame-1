def sendNow():
	user = input('masukkan nama anda')
	warehousing = {
		'harga':1000000,
		'total':15
	}
	cleansing = {
		'harga':1500000,
		'total':10
	}
	integration = {
		'harga':2000000,
		'total':15
	}
	transformation = {
		'harga':2500000,
		'total':10
	}
	sub_warehousing = warehousing['harga'] * warehousing['total']
	sub_cleansing = cleansing['harga'] * cleansing['total']
	sub_integration = integration['harga'] * integration['total']
	sub_transformation = transformation['harga'] * transformation['total']
	sub_total = sub_warehousing + sub_cleansing + sub_integration + sub_transformation
	print('Tagihan Kepada:', user)
	print("Selamat pagi, anda harus membayar tagihan sebesar:")
	print(sub_total)

print('---------Menu--------')
print('[1]Kirim sekarang')
print('[2]Kirim nanti')
choose = input('pilih')
if choose == '1':
	sendNow()
	# print('ok')
elif choose == '2':
	print('nanti aku kirim')
else:
	print('ga ada pilihan')
print('pilihan anda ', choose)

# total = tagihan[0] + tagihan[1] + tagihan[2] + tagihan[3] +tagihan[4]
# print(total)
def perulanganWhile():
	tagihan = [50000 ,75000, 125000, 300000, 200000]
	total_tagihan = 0
	i=0
	jumlah_tagihan = len(tagihan)
	while i < jumlah_tagihan:
		total_tagihan += tagihan[i]
		i += 1

	print(total_tagihan)

perulanganWhile()