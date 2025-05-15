import tkinter as tk
from tkinter import messagebox
import sys

arquivo_cadastros = "cadastros.txt"

def realizar_cadastro():
    nome = entrada_nome_cadastro.get()
    email = entrada_email_cadastro.get()

    if nome and email:
        try:
            with open(arquivo_cadastros, "a") as arquivo:
                arquivo.write(f"{nome},{email}\n")
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            janela_cadastro.destroy()
        except Exception as e:
            messagebox.showerror("Erro ao salvar", f"Não foi possível salvar o cadastro: {e}")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

janela_cadastro = tk.Tk()
janela_cadastro.title("Cadastro")
janela_cadastro.geometry("300x220")
janela_cadastro.configure(bg="#cccccc")

rotulo_cadastro = tk.Label(janela_cadastro, text="Preencha os dados:",bg= "#cccccc", font=("Forte", 18))
rotulo_cadastro.pack(pady=10)

label_nome_cadastro = tk.Label(janela_cadastro, text="Nome:", bg= "#cccccc", font=("Arial", 12))
label_nome_cadastro.pack()

entrada_nome_cadastro = tk.Entry(janela_cadastro, width=20, font=("Arial", 14))
entrada_nome_cadastro.pack()

label_email_cadastro = tk.Label(janela_cadastro, text="Email:", bg= "#cccccc", font=("Arial", 12))
label_email_cadastro.pack()

entrada_email_cadastro = tk.Entry(janela_cadastro, width=20, font=("Arial", 14))
entrada_email_cadastro.pack()

botao_realizar_cadastro = tk.Button(janela_cadastro, text="Realizar Cadastro", bg="#c1bcf7", command=realizar_cadastro)
botao_realizar_cadastro.pack(pady=10)

janela_cadastro.mainloop()
