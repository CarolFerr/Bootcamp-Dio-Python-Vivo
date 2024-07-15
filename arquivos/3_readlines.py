arquivo = open("lorem.txt", "r")
# print(arquivo.readlines())

for linha in arquivo.readlines():
    print(linha)
arquivo.close()
