class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    # Para quando see quer setar a idade automaticamente, sem a necessidade
    # de colocar no construtor
    def idade(self):
        _ano_atual = 2045
        return _ano_atual - self._ano_nascimento


pessoa = Pessoa("Ana", 1991)
print(f"Nome: {pessoa.nome}\tIdade: {pessoa.idade}")
