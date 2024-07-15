class Pessoa:
    especie = "Homo sapiens"  # Instância de classe (compartilhada)

    def __init__(self, nome, idade):
        self.nome = nome  # Instância de atributo (individual)
        self.idade = idade  # Instância de atributo (individual)


pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.especie)  # Homo sapiens
print(pessoa2.especie)  # Homo sapiens

# Alterando a instância de classe
Pessoa.especie = "Homo Deus"

print(pessoa1.especie)  # Homo Deus
print(pessoa2.especie)  # Homo Deus


class Pessoa:
    especie = "Homo sapiens"  # Instância de classe (compartilhada)

    def __init__(self, nome, idade):
        self.nome = nome  # Instância de atributo (individual)
        self.idade = idade  # Instância de atributo (individual)


pessoa1 = Pessoa("João", 30)
pessoa2 = Pessoa("Maria", 25)

print(pessoa1.nome)  # João
print(pessoa2.idade)  # 25
