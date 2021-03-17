list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang']
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
#! method index
score_pertama_sud = list_score.index('Sud') 

#! method insert
#! menambahkan elemen
list_score.insert(3, 'Sud')

#! method pop
#! pop adalah menghilangkan element berdasarkan index
list_menu.pop(1)

#! method reverse
list_menu.reverse()

#?print
print(list_score)
print(list_menu)