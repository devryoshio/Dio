import sqlite3

conexao = sqlite3.connect("teste/clientes.db")


cursor = conexao.cursor()

#
# cursor.execute("CREATE TABLE clientes(id INTEGER PRIMARY KEY  AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")


data = (1,)

cursor.execute("DELETE FROM clientes WHERE id=?;", data)
conexao.commit()