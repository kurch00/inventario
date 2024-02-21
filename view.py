# CRUD 
import sqlite3 as lite

conexao = lite.connect('dados.db')


def inserir_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "INSERT INTO inventario(nome, local, descricao, marca, data_compra, valor_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


def atualizar_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "UPDATE inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


def deletar_form(i):
    with conexao:
        cur = conexao.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, i)


def ver_form():
    ver_dados = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


def ver_item(id):
    ver_dados_individual = []
    with conexao:
        cur = conexao.cursor()
        query = "SELECT * FROM inventario WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)

    return ver_dados_individual
