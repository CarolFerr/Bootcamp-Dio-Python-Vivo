def calculadora(operacao):
    def soma(a, b):
        return a + b

    def subtracao(a, b):
        return a - b

    def multiplicacao(a, b):
        return a * b

    def divisao(a, b):
        return a / b

    if operacao == '+':
        return soma

        # ou utilizando a função match

    '''match operacao:
        case '+':
            return soma
        case '-':
            return subtracao
        case '*':
            return multiplicacao
        case '/':
            return divisao'''


op = calculadora("+")
print(op(2, 2))

