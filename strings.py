#EXERCICIO 1

from cgitb import text


nome = input("Insira o seu nome: ").upper()
print(nome[::-1])

#EXERCICIO 2

palindromo = input("Insira um palindromo: ")
reverse = palindromo[::-1]

if(palindromo==reverse):
    print("É um palindromo")
else:
    print("Não é um palindromo")

#EXERCICIO 3

palavra = input("informe uma palavra: ")
print(f"Primeiro : {palavra[0]}")
print(f"Ultimo : {palavra[-1]}")

#EXERCICIO 4

texto = input("Informe o texto: ")

for word in texto:
    if(word != "*"):
        first=texto.find(word)
        break

print(texto[first:])
