#EXERICIO 1
numeros = [1, 4, 0, 6, 2, 0]
dividendo = int(input("Informe um dividendo: "))

for numero in numeros:
    try:
        divisao = dividendo/numero
        print(divisao)
    except(ZeroDivisionError):
        print("Não é possível dividor por Zero")
#EXERICIO 2
try:
    print(name)
except (ValueError):
    print("Nome errado")
try:
    import mathes
except ModuleNotFoundError:
    print("Modulo nao encontrando")
    print("Importando o correto math...")
    import math
try:
    f = open('notfound.txt','r')

except FileNotFoundError:
    print("File não existe")
    print("Usando o argumento 'a' para criar")
    f = open('notfound.txt','a')
    f.close()
#EXERCICIO 3
print("Aprendendo exceções")
try:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    quociente = num1 / num2
    print ("Ambos os números foram informados corretamente")
except ValueError:
    print("Por favor informe apenas números")
except ZeroDivisionError:
    print("O segundo número não deve ser zero")
else:
    print(" Great .. you are a good programmer")
# sempre executa no final
print("Fim do programa")