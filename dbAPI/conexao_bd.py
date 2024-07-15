import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), '
        'email VARCHAR(100))')
    conexao.commit()


# O ponto de interrogação evita injeção de SQL
def inserir_dado_tabela(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute(
        'INSERT INTO cliente (nome, email) VALUES (?,?);', data)
    conexao.commit()


def atualizar_dado_tabela(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE cliente SET nome=?, email=? WHERE id=?;', data)
    conexao.commit()


def excluir_dado_tabela(cursor, conexao, id):
    # Tupla com um unico dado deve ser seguido por uma virgula
    data = (id,)
    cursor.execute('DELETE FROM cliente WHERE id=?;', data)
    conexao.commit()


def inserir_muitos_dados_tabela(cursor, conexao, dados):
    # Lista de tuplas com os valores a serem inseridos
    cursor.executemany('INSERT INTO cliente (nome, email) VALUES (?,?);', dados)
    conexao.commit()

# Consultando Registros
# Consultando coom unico resultado


def recuperar_cliente(cursor, id):

    cursor.execute('SELECT * FROM cliente WHERE id=?', (id,))
    return cursor.fetchone()


# Consultando com multiplos resultados


def listar_cliente(cursor):
    # return cursor.execute('SELECT * FROM cliente ORDER BY nome;')
    cursor.execute('SELECT * FROM cliente ORDER BY nome')
    return cursor.fetchall()


# usuarios = listar_cliente(cursor)
# for usuarios in usuarios:
#     print(dict(usuarios))


usuario = recuperar_cliente(cursor, 1)
print(dict(usuario))
print(usuario['id'], usuario['nome'], usuario['email'])

# inserir_dado_tabela(conexao, cursor, 'Patricia', 'patty_cia@yahoo.com')
# atualizar_dado_tabela(conexao, cursor, 'Ana Joaquina', 'anajo@outlook.com', 1)
# excluir_dado_tabela(cursor, conexao, 2)
# dados = [
#     ('Valeria', 'val_eria@hotmail.com'),
#     ('André', 'dre12@gmail.com'),
#     ('Hugo', 'hugo_rico@hotmail.com')]
# inserir_muitos_dados_tabela(cursor, conexao, dados)
