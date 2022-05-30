#EXERCICIO 1
senha = input("Informe uma senha: ")

if(len(senha)<10):
    print(f"A senha contém {len(senha)} caracteres")
    print("Caracter minimo é 10!")

#EXERCICIO 2

dia = input("Informe o dia de nascimento: ")
mes = input("Informe o mẽs de nascimento: ")
ano = input("Informe o ano de nascimento : ")

print(f"A data de nascimento é : {dia}/{mes}/{ano}")