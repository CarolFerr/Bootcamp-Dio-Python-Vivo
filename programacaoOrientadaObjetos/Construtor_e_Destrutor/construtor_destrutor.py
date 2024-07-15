class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def falar(self):
        print('auau')

    def __del__(self):
        print('Removendo a instância da classe')


def criar_cachorro():
    c = Cachorro('Aladim', 'Preto', False)
    print(c.nome)


c = Cachorro('Max', 'amarelo')
c.falar()

print('Ola Mundo!')
del c
print('Ola Mundo!')
print('Ola Mundo!')
print('Ola Mundo!')

criar_cachorro()
