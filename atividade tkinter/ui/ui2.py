import tkinter as tk 
import mysql.connector
from tkinter import messagebox

entry_nome = tk.Entry()  # Create the Entry widget for entry_nome

def salvar_nome():
    nome = entry_nome.get()
    if nome:
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3306,
                database="cadastro"
            )
            cursor = conexao.cursor()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
        finally:
            if 'conexao' in locals() and conexao.is_connected():
                conexao.close()