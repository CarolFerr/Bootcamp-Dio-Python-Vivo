def meu_gerador(numbers):
    for num in numbers:
        yield num


# Criando um gerador (a sintaxe é a mesma de uma função)
my_gen = meu_gerador([1, 2, 3])

# Iterando pelo gerador (podemos usar um loop for diretamente)
for element in my_gen:
    print(element)
