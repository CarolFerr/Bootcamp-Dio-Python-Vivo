def pai():
    print("Escrevendo da pai() função")

    def filho1():
        print("Escrevendo da filho1() função")

    def filho2():
        print("Escrevendo da filho2() função")

    filho2()
    filho1()


pai()


# Funcao Interna

def principal():
    print('executando a funcao principal')

    def funcao_interna():
        print('executando a funcao interna')

    def funcao_2():
        print('executando a funcao 2')

    funcao_interna()
    funcao_2()


principal()

