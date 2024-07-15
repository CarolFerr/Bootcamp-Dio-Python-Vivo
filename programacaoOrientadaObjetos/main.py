'''Exercicios Visagio'''
'''1'''


def encontrar_maior(dicionario):
    if not dicionario:
        return None, None

    nome_maior_numero, maior_numero = next(iter(dicionario.items()))

    for nome, numero in dicionario.items():
        if numero > maior_numero:
            maior_numero = numero
            nome_maior_numero = nome

    return nome_maior_numero, maior_numero


dicionario_valores = {'Alice': 8, 'Bob': 35, 'Charlie': 20, 'Pedro': 8, 'David': 35}
nome, valor = encontrar_maior(dicionario_valores)
print(f'O maior valor é {valor} associado ao nome {nome}')

'''2'''


class PilhaEstacionamento:
    def __init__(self):
        self.carros = []

    def entrar_estacionamento(self, carro):
        self.carros.append(carro)

    def sair_estacionamento(self):
        if not self.carros:
            return 'Estacionamento Vazio.'
        else:
            # retira do topo da pilha como deve ser -> LIFO -> ultimo a entrar é o primeiro a sair
            # return f'O carro {self.carros.pop()} saiu do estacionamento' # carro XYZ789
            # Inverte a ordem, ou seja, o primeiro a entrar é o primeiro a sair rompendo com a estrutura da pilha,
            # mas criando uma fila -> FIFO
            return f'O carro {self.carros.pop()} saiu do estacionamento'  # ABC123


carro = PilhaEstacionamento()
carro.entrar_estacionamento('ABC123')  # entrou primeiro
carro.entrar_estacionamento('XYZ789')  # entrou depois
carro.entrar_estacionamento('FGH654')

print(carro.sair_estacionamento())


