#EXERCICIO 1
tupla = ("red", [10, 20, 30], (5, 15, 25))
print(tupla[1][1])
#EXERCICIO 2
tupla1 = (11, 22)
tupla2 = (99, 88)
print(tupla1,tupla2)
t1_0,t1_1 = tupla1
t2_0,t2_1 = tupla2
tupla1 = tuple([t2_0,t2_1])
tupla2 = tuple([t1_0,t1_1])
print(tupla1,tupla2)
#EXERCICIO 3
tupla = (11, [22, 33], 44, 55)
print(tupla)
#tupla[1] = ([tupla[1][0]*2,tupla[1][1]*2])
tupla[1][0] = tupla[1][0]*2
tupla[1][1] = tupla[1][1]*2
item1,item2 = tupla[1]
print(tupla)
print(f"Item 1 : {item1}",f"\nItem 2 : {item2}")
#EXERCICIO 4
tupla1 = (11, 22, 33)
tupla2 = (44, 55)
new_tupla =  tuple(tupla1+tupla2)
print(new_tupla)
#EXERCICIO 5
tupla_duplicated = tuple(new_tupla*2)
print(tupla_duplicated)