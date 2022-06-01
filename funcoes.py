#EXERICIO 1
def soma(*numeros):
    soma=0
    for numero in numeros:
        soma+=numero
    print(f"Soma dos numeros foram : {soma}")
soma(1,2,3,4)

#EXERCICIO 2 

def func (numero):
    if numero > 0:
        print("P")
    else:
        print("N")
func(10)
func(-10)
#EXERICIO 3
def calcula (*numero,op):
    if op == 'adicao':
        soma = 0
        for num in numero:
            soma += num
        print(soma)
    elif op == 'subtracao':
        sub = 0 
        for num in numero:
            sub -= num
        print(sub)
    elif op == 'multiplicao':
        mult = 1 
        for num in numero:
            mult *= num
        print(mult)
    elif op == 'divisao':
        div = 1 
        for num in numero:
            div /= num
        print(div)
calcula(1,5,op='multiplicao')
#EXERCICIO 4
def multi_nomes(*nomes,mult):
    for nome in nomes:
        print(nome*mult)
multi_nomes('João','Maria',mult=2)