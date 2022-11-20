import sqlite3

def connect():
    conn = sqlite3.connect('salarios.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Salaries")
    tabela = cursor.fetchall()
    cursor.close()
    conn.close()
    return tabela
