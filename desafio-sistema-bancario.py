def barrinha(texto):
    print("-" * 60)
    print(texto.center(60))
    print("-" * 60)


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    barrinha("Menu")

    opcao = input('''1. Depositar\n2. Sacar\n3. Extrato\n0. Finalizar\nOpcao: ''')

    if opcao == "1":
        barrinha("Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        barrinha("Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("ERRO! Saldo Insuficiente.")

        elif excedeu_limite:
            print("ERRO! O valor excede o limite.")

        elif excedeu_saques:
            print("ERRO! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("ERRO! O valor informado é inválido.")

    elif opcao == "3":
        barrinha("Extrato")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

