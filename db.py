import sqlite3
conn = sqlite3.connect('salarios.sqlite') #Define conexão como global
        
def connect():
    cursor = conn.cursor()
    return conn, cursor

def fechar(cursor):    
    cursor.close()
    conn.close()

def create():
    connect()
    cursor.execute("CREATE TABLE IF NOT EXISTS Salaries (Id INTEGER PRIMARY KEY,EmployeeName TEXT,JobTitle TEXT,BasePay NUMERIC,OvertimePay NUMERIC,OtherPay NUMERIC,Benefits NUMERIC,TotalPay NUMERIC,TotalPayBenefits NUMERIC,Year INTEGER,Notes TEXT,Agency TEXT,Status TEXT) CREATE INDEX salaries_year_idx ON Salaries (Year);")
    fechar(cursor)

def listaTabelas():
    cursor = connect()
    cursor.execute("""select tbl_name, [sql] from sqlite_schema where type = 'table'""")
    tabela(cursor.fetchall())
    fechar(cursor)
    return tabela

def tabela(nmTabela):
    cursor = connect()
    cursor.execute("""SELECT * FROM {nmTabela}""")
    tabela = cursor.fetchall()
    print(tabela)
    fechar(cursor)
    return tabela
    