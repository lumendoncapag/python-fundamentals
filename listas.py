#EXERCICIO 1
numeros = [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]
new_numeros = [i for i in numeros if i < 10]
print(new_numeros)
#EXERCICIO 2
mult_2=[]
for x in numeros:
    mult_2.append(x*2)
print(mult_2)
#EXERCICIO 3
nomes_3 = ["Michael", "", "Ana", "Joao", "", "Marcia"]
new_nome3 = [name for name in nomes_3 if name != ""]
print(new_nome3)
#EXERCICIO 4
nomes = [
    ["Michael", "Ana", "Joao", "Marcia"],
    ["Fabio", "Luiz", "Lucia", "Malu"],
    ["Jorge", "Maria", "Jose"],
]
lista_completa = []
for item in nomes:
    for subitem in item:
        lista_completa.append(subitem)
print(lista_completa)