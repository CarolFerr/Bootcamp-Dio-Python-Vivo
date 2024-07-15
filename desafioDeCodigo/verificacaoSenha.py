import re


def verificar_forca_senha(senha):
    comprimento_minimo = 8
    tem_letra_maiuscula = False
    tem_letra_minuscula = False
    tem_numero = (re.search(r'[0-9]', senha))
    tem_caractere_especial = (re.search(r'[!@#$%^&*(),.?\":{}|<>]', senha))

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return f"Sua senha é muito curta. Recomenda-se no mínimo {comprimento_minimo} caracteres."

    # Verificando se a senha contém letras maiúsculas e minúsculas
    tem_letra_maiuscula = (re.search(r'[A-Z]', senha))
    tem_letra_minuscula = (re.search(r'[a-z]', senha))

    # Verificando se a senha contém sequências comuns
    sequencias_comuns = ["123456", "abcdef"]
    for sequencia in sequencias_comuns:
        if sequencia in senha:
            return "Sua senha contém uma sequência comum. Tente uma senha mais complexa."

    # Verificando se a senha contém palavras comuns
    palavras_comuns = ["password", "123456", "qwerty"]
    if senha in palavras_comuns:
        return "Sua senha é muito comum. Tente uma senha mais complexa."

    # Se a senha atende a todos os critérios, retorna uma mensagem de sucesso
    if (tem_letra_maiuscula or tem_letra_minuscula) and (tem_numero and tem_caractere_especial):
        return "Sua senha atende aos requisitos de segurança. Parabéns!"
    elif (tem_letra_minuscula or tem_letra_maiuscula) and tem_numero and not tem_caractere_especial:
        return "Sua senha nao atende aos requisitos de segurança."


# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)
