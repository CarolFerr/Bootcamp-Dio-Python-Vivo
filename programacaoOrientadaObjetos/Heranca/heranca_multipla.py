class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        # Automatizado/dinamicamente -> se a classe crescer não é necessário  manipular
        # Pega a classe e o nome dela e utiliza compreensão de lista para acessar os atributos
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)



class Ave(Animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        # Qualquer atributo novo, vai ser passado por chave e valor
        super().__init__(**kwargs)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)  # traz a ordem de resolução
        # print(Ornitorrinco.mro())
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)




gato = Gato(nro_patas=4, cor_pelo='preto')
print(gato)
# Parâmetros passados de forma nomeado
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo='marrom', cor_bico='laranja')
print(ornitorrinco)

