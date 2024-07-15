class Bicicleta:
    # Atributos da classe
    # self = referencia explicita = this
    def __init__(self, cor, modelo, ano, valor, marcha):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    # Metodos da classe = Comportamentos
    def buzinar(self):
        print('Plim plim')

    def parar(self):
        print('Parando a bicicleta...')
        print('Bicicleta Parada')

    def correr(self):
        print('Vrummmm...')

    def trocar_marcha(self, nro_marcha):
        print('Trocando Marcha...')
        if nro_marcha > self.marcha:
            print('Marcha trocada!')
        else:
            print('Não foi possível realizar a troca de marcha!')

    # Método para mostrar as caracteristicas do objeto da classe
    '''def __str__(self):
        # Manualmente
        return f'Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}'
        '''

    def __str__(self):
        # Automatizado/dinamicamente -> se a classe crescer não é necessário  manipular
        # Pega a classe e o nome dela e utiliza compreensão de lista para acessar os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


'''# Instancia de bicicleta
b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
# Acessando os atributos
print(b1.cor, b1.modelo, b1.ano, b1.valor)'''

b2 = Bicicleta('verde', 'monark', 2000, 189, 3)
Bicicleta.buzinar(b2)  # b2.buzinar
print(b2.cor)  # atributos em python são acessados publicamente
# Chamando o objeto
print(b2)
b2.trocar_marcha(nro_marcha=5)
