import sqlite3
def create():
    conn = sqlite3.connect('salarios.sqlite')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Salaries (Id INTEGER PRIMARY KEY,EmployeeName TEXT,JobTitle TEXT,BasePay NUMERIC,OvertimePay NUMERIC,OtherPay NUMERIC,Benefits NUMERIC,TotalPay NUMERIC,TotalPayBenefits NUMERIC,Year INTEGER,Notes TEXT,Agency TEXT,Status TEXT) CREATE INDEX salaries_year_idx ON Salaries (Year);")
    cursor.close()
    conn.close()
def connect():
    conn = sqlite3.connect('salarios.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Salaries")
    tabela = cursor.fetchall()
    cursor.close()
    conn.close()
    return tabela

