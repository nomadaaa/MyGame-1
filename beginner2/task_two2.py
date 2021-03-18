info_karyawan = {'nama' : 'Aksara','nik' : '1211011','pekerjaan' : 'Data Analyst'}
info_karyawan.clear()

#!copy
info_karyawan1 = {'nama' : 'Aksara','nik' : '1211011','pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Cahyo'
info_karyawan2['nik'] = '201621058'

#! keys
kunci = info_karyawan2.keys()

#! values
isi = info_karyawan1.values()
print(isi)
