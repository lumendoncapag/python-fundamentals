#EXERCICIO 1
from dataclasses import dataclass
import datetime
class Veiculo:
    def __init__(self,ano,quilometragem):
        self.ano = ano
        self.quilometragem = quilometragem
    def verificacao(self):
        ano_atual = int((str(datetime.date.today()).split("-"))[0])
        if((ano_atual-self.ano)>7 or self.quilometragem > 100000):
            print("O carro precisa ser trocado!!")
            if(self.quilometragem>100000):
                print("Sua quilometragem ta acima de 100 mil Km")
            elif(ano_atual-self.ano>7):
                print("O seu carro já passou dos 7 anos de uso")
        else:
            print("O carro ainda está em perfeito estado!")
gol = Veiculo(2000,1000)
gol.verificacao()

#EXERCICIO 2
class Animal:
    def __init__(self,nome,especie):
        self.nome = nome
        self.especie = especie
comando = ""
lista_animals = []
while (comando!='nao'):
    especie,nome = input("Informe a espécie e o nome do seu animal (Ex: Gato,Sakura) :  ").split(",")
    lista_animals.append(Animal(nome,especie))
    comando = input("Deseja adicionar mais um ? ")
for animal in lista_animals:
    print(f'{(animal.especie).capitalize()} com nome "{(animal.nome).capitalize()}"')