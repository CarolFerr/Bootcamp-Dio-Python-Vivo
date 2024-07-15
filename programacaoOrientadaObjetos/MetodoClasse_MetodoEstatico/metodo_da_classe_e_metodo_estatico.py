class Person:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    # Método de Classe -> preciso acesso ao contexto da classe
    @classmethod
    def criar_apartir_data_nasc(cls, nome, mes, dia, ano):
        idade = 2024 - ano
        return cls(nome, idade)

    # Método Estático -> não preciso nem contexto, nem de classe , nem instânica objeto
    def e_maior_idade(idade):
        return idade >= 18


p = Person("Ana", 70)
print(p.nome, p.idade)

p2 = Person.criar_apartir_data_nasc("Carla", 12, 10, 1958)
print(p2.nome, p2.idade)

print(Person.e_maior_idade(18))  # retorno booleano
