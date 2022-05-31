#EXERCICIO 1
lista = [1,2,3,4,5]
sub_lista = []
for item in lista:
    printar= " "
    sub_lista.append(item)
    for sub_item in sub_lista:
        printar+=f"{sub_item} "
    print(printar)

#EXERCICIO 2
numero = int(input("Informe um numero : "))
soma = 0
for n in range (numero+1):
    soma+=n
print(soma)

#EXERCICIO 3
print(f"Numeros pares na lista : {lista}")
for numero in lista:
    if numero%2 == 0:
        print(numero)

#EXERCICIO 4
comando=""
while(comando != "sair"):
    comando = input("Digite o comando: ")
    if(comando == "sair"):
        print("Fim do Programa")

#EXERCICIO 5

for i in lista:
    for x in lista:
        print(f"{i} x {x} = {i*x}")

        #LUMENDONCA