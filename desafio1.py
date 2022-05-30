mapa_nomes={
    'joao':{
    'nome': 'joao',
    'apelidos': ['joaozinho', 'jj'],
    'idade': 13,
    'materias': {
        'matematica': 8.7,
        'geografia': 7.3,
        'ciencias': 9.0,
        }
    },
    'maria':{
    'nome': 'maria',
    'apelidos': ['mama', 'mah'],
    'idade': 13,
    'materias': {
        'matematica': 6.8,
        'geografia': 10,
        'ciencias': 8.4,
        }
    }
}
def busca_nome(nome_busca):
    for nome_principal in mapa_nomes.keys():
        if nome_principal == nome_busca:
            print(mapa_nomes.get(nome_busca).get("nome"))
        

def busca_idade(idade):
    names = []
    for nome_principal,dic_interno in mapa_nomes.items():
        for key,value in dic_interno.items():
            if key == 'idade':
                if (value==idade):
                    names.append(dic_interno['nome'])
    print(names)

def buscar_maior_nota(materia):
    dic = {
        'nome':'',
        'nota':0
    }
    for nome_principal,dic_interno in mapa_nomes.items():
        for key,value in dic_interno.items():
            if (key == 'materias'):
                for materias,nota in value.items():
                    if materias == materia:
                        if(nota>dic.get('nota')):
                            dic['nota'] = nota
                            dic['nome'] = nome_principal
    print(f"Maior nota de {materia} foi {dic.get('nota')}, pertecente a {dic.get('nome')}!!")

busca_idade(13)
busca_nome('maria')
buscar_maior_nota('geografia')