def duplicar(funcao):
    # inner function
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        return funcao(*args, **kwargs)
        # retorna o valor da função que esta sendo passada

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()


tecnologia = aprender("Python")
print(tecnologia)


def meu_decorador(funcao):
    # inner function
    def envelope(*args, **kwargs):
        # checar conexões, por exemplo
        print("Faz algo antes de executar a função")
        resultado = funcao()  # usada por parametro
        # enviar alguma notificacao para outro sistema, por exemplo
        print("Faz algo depois de executar a função")
        return resultado

    return envelope


def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo! {nome}")
    return nome.upper()


resultado = ola_mundo("Carla", 1000)
print(resultado)
