arquivo = open("lorem.txt", "r")
print(arquivo.readline())
# Se len for zero encerra o programa, pois zero é falso
# simbolo walrus (:=) : atribui valores a variáveis de forma concisa e legível
# while len(linha := arquivo.readline()):  # Lê uma linha e coloca /n, ou seja pula uma linha
#     print(linha)
arquivo.close()
