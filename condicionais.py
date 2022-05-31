#EXERICIO 1
A,B,C = input("Informe 3 números: ").split(" ")
A = int(A); B = int(B); C=int(C)
if(A>B and A>C):
    print(f"A é maior = {A}")
elif(B>A and B>C):
    print(f"B é maior = {B}")
elif(C>A and C>B):
    print(f"C é maior = {C}")
else:
    print(f"Todos são iguais = {A}")
#EXERCICIO 2
print(5==5)
print(5>4 or 2>2)
print((True and 5<=6) and (10>4))
print(7>6>2)
#EXERCICIO 3
for numero in [1, 2, 3, 4, 5, 6, 7]:
    if numero%2 == 0:
        print(numero)