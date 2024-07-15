import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# COLUNA_ID = 0
# COLUNA_NOME = 1

# try:
#     with open(ROOT_PATH / "usuarios.csv", "w", newline= '', encoding="utf-8") as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(["id", "nome"])
#         escritor.writerow(["1", "Ana"])
#         escritor.writerow(["2", "Valentina"])
# except IOError as exc:
#      print(f"Erro ao criar o arquvio. {exc}")

# try:
#     with open(ROOT_PATH / "usuarios.csv", "r", encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
# except IOError as exc:
#     print(f"Erro ao criar o arquvio. {exc}")

# try:
#     with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as arquivo:
#         leitor = csv.reader(arquivo)
#         for idx, row in enumerate(leitor):
#             if idx == 0:  # cabecalho
#                 continue
#             print(f'ID: {row[COLUNA_ID]}')
#             print(f'NOME: {row[COLUNA_NOME]}')
# except IOError as exc:
#     print(f"Erro ao criar o arquvio. {exc}")

try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"NOME: {row['nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquvio. {exc}")
