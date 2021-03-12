list_cash_flow = [
2500000, 5000000, -1000000, -2500000, 5000000, 10000000,
-5000000, 7500000, 10000000, -1500000, 25000000, -2500000
]
total_pemasukan, total_pengeluaran = 0, 0
for dana in list_cash_flow:
	if dana > 0:
		total_pemasukan += dana
	else:
		total_pengeluaran += dana
	total_pengeluaran *= -1
	print('Pemasukan',total_pemasukan)
	print('Pengeluaran', total_pengeluaran)


