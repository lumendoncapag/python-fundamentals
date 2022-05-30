#EXERCICIO 1
estudante = {
    "nome": "Maria",
    "notas": {
        "fisica": 70,
        "historia": 80
    }
}
print(f"A nota do estudante em historia foi : {estudante['notas']['historia']}")
#EXERCICIO 2
funcionarios = {
    'mario': {'nome': 'Mario', 'salario': 7500},
    'ana': {'nome': 'Ana', 'salario': 8000},
    'bete': {'nome': 'Elizabeth', 'salario': 6500}
}
funcionarios['ana']['salario'] = 9500
print(f"O salario atual de ana é : {funcionarios['ana']['salario']}")
#EXERCICIO 3
novos_funcionarios = {
    'juliana': {'nome': 'Juliana', 'salario': 7000},
    'joao': {'nome': 'João', 'salario': 6200}
}
funcionarios.update(novos_funcionarios)
print(funcionarios['juliana'])
#EXERCICIO 4
remocao = ['joao', 'bete']
for key,value in list(funcionarios.items()):  #USAR LIST PARA NAO CORROMPER O DICIONARIO
    for func in remocao:
        if(key==func):
            funcionarios.pop(func)
print(funcionarios)
