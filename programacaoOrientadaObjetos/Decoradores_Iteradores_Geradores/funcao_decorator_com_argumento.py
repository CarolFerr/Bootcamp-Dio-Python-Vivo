def duplicar(funcao):
    # inner function
    # *args e **kwargs deixa a parametrização mais generica
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")


aprender("Python")
