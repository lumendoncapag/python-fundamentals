import string
#EXERCICIO 1
with open('/home/lumendonca/Desktop/python-fundamentals/arquivo.txt','r') as reader:
    for i in range(10):
        print(reader.readline())
reader.close()
#EXERCICIO 2
with open('/home/lumendonca/Desktop/python-fundamentals/arquivo.txt','r') as reader:
    arquivo=reader.readlines()
    cont=0
    for i in arquivo:
        cont+=1
print(f"O arquivo tem {cont} linhas")
reader.close()
#EXERCICIO 3
with open('/home/lumendonca/Desktop/python-fundamentals/arquivo.txt','a') as writer:
    frase = "Hello world"
    writer.write("\n"+frase)
writer.close()
with open('/home/lumendonca/Desktop/python-fundamentals/arquivo.txt','r') as reader:
    for line in reader.readlines():
        print(line)
reader.close()
#EXERCICIO 4
alfabeto = list(string.ascii_lowercase)
print(alfabeto)
for letra in alfabeto:
    with open(f'/home/lumendonca/Desktop/python-fundamentals/folder_arquivos/{letra}.txt','w') as write:
        write.write(letra)
    write.close()
    