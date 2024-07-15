# Tipos de erros mais comuns:

# Tipo de erro 1:
try:
    with open("meu-arquivo", "r", encoding='utf-8') as arquivo:
        print(arquivo.read())
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")
    # Capiturando os detalhes da exceção gerada
    print(exc)
except IOError:
    print("Erro ao abrir o arquivo")


# Tipo erro 2:
# ROOT_PATH = Path(__file__).parent
# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
