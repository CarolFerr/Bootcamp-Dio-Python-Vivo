class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o Motor...')

    def __str__(self):
        # Automatizado/dinamicamente -> se a classe crescer não é necessário  manipular
        # Pega a classe e o nome dela e utiliza compreensão de lista para acessar os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # Método próprio da classe
    def __init__(self, carregado, cor, placa, numero_rodas):
        # Chama a implementação da classe pai
        super().__init__(cor, placa, numero_rodas)  # definido a ordem que se deseje, antes ou depois
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Criando o objeto
moto = Motocicleta('branca', 'abc1234', 2)
carro = Carro('preto', 'xde987', 4)
caminhao = Caminhao(True, 'vermelho', 'dpe654', 8)

# caminhao.esta_carregado()

print(caminhao)
print(carro)
print(moto)
