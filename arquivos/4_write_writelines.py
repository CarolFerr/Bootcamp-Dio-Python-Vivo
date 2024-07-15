arquivo = open("lorem.txt", "w")
arquivo.write("Adicionando um dado no arquivo lorem com a funcao write")
arquivo.writelines(["\n", "Adicinando ", "um ", "novo ", "dado ", "ao ", "arquivo ",
                    "lorem ", "com ", "writelines"])
arquivo.close()

