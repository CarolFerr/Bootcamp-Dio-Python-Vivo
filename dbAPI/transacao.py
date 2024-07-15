import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row
try:
    cursor.execute('INSERT INTO cliente (nome, email) VALUES(?,?)', ('Teste 3', 'teste1@gmail.com'))
    cursor.execute('INSERT INTO cliente (id, nome, email) VALUES(?,?,?)', ('6', 'Teste 4', 'teste1@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Um erro ocorreu! {exc}")
    conexao.rollback()



