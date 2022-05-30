#EXERCICIO 1
volei = {'artur', 'bruna', 'david', 'julia', 'max', 'paulo'}
futebol = {'artur', 'cleia', 'david', 'lucas', 'mateus', 'rafael'}
natacao = {'bianca', 'cielo', 'cleia', 'lucas', 'phelps', 'tulio'}
print("Alunos que praticam volei ou futebol : ")
print(volei | futebol)
print("Alunos que praticam futebol e natacao : ")
print(futebol & natacao)
print("Alunos que praticam volei mas nao futebol : ")
print(volei - futebol)