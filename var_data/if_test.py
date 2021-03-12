x = int(input('masukkan nilai'))
if x % 2 == 0:
	print('x habis dibagi 2')
elif x % 3 == 0:
	print('x habis dibagi 3')
elif x % 5 == 0:
	print('x habis dibagi 5')
else:
	print('x tidak bisa habis dibagi')

	
jam = int(input('Masukkan jam'))
if jam >= 5 and jam < 12:
	print('selamat pagi')
else:
	print('Selamat datang')