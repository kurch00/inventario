import sqlite3 as lite

conexao = lite.connect('dados.db')

with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_compra DATE, valor_compra DECIMAL, serie TEXT, imagem TEXT)")
