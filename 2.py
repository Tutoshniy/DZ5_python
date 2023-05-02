
list_1 = ['Иван', 'Михаил', 'Григорий']
list_2 = [10000, 20000, 30000]
list_3 = ['10%', '14.5%', '20.15%']
my_gen = {list_1[i]: list_2[i] * (float(list_3[i].replace('%', '')) / 100.) for i in range(len(list_1))}
print(my_gen)


