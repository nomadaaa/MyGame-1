
#!union
#!Mengembalikan hasil penggabungan (union) dari dua buah set. 
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel3 = parcel1.union(parcel2)
print(parcel3)

#! isdisjoint()
#! Mengembalikan nilai kebenaran apakah 
#! suatu set disjoint (saling lepas/tidak mengandung elemen yang sama) dengan set lainnya.
check = parcel1.isdisjoint(parcel2)
print(check)
