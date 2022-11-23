#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

class ConectarDB:
    def __init__(self):
        self.con = sqlite3.connect('salarios.sqlite')
        self.cur = self.con.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS Salaries (
                Id INTEGER PRIMARY KEY,
                EmployeeName TEXT,
                JobTitle TEXT,
                BasePay NUMERIC,
                OvertimePay NUMERIC,
                OtherPay NUMERIC,
                Benefits NUMERIC,
                TotalPay NUMERIC,
                TotalPayBenefits NUMERIC,
                Year INTEGER,
                Notes TEXT,
                Agency TEXT,
                Status TEXT);''')
        except Exception as e:
            print(f'[x] Falha ao criar tabela [x]: {e}')
        else:
            print('[!] Tabela criada com sucesso [!]\n')

    def criar_indice(self):
        try:
            self.cur.execute('''CREATE INDEX salaries_year_idx ON Salaries (Year);''')
        except Exception as e:
            print(f'[x] Falha ao criar indice [x]: {e}')
        else:
            print('[!] Índice criado com sucesso [!]\n')

    def inserir_registro(self, registro):
        try:
            self.cur.execute(
                '''INSERT INTO Salaries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', registro)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_varios_registros(self, registro):
        try:
            self.cur.executemany(
                '''INSERT INTO Salaries VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', registro)
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registro_pela_id(self, Id):
        return self.cur.execute('''SELECT * FROM Salaries WHERE Id=?''', (Id,)).fetchone()

    def consultar_registros(self, limit=10):
        return self.cur.execute('''SELECT * FROM Salaries LIMIT ?''', (limit,)).fetchall()

    def alterar_registro(self, Id, nome, sexo):
        try:
            self.cur.execute(
                '''UPDATE Salaries SET nome=?, sexo=? WHERE Id=?''', (nome, sexo, Id))
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_registro(self, Id):
        try:
            self.cur.execute(
                f'''DELETE FROM Salaries WHERE Id=?''', (Id,))
        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')

