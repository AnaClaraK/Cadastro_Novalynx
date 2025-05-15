import tkinter as tk
import os
from tkinter import messagebox

arquivo_cadastros = "cadastros.txt"

lista = []

def atualizar_lista():
    lista_cadastros_listbox.delete(0, tk.END)
    for i, item in enumerate(lista):
        lista_cadastros_listbox.insert(tk.END, f"{i+1}- Nome: {item['nome']}, Email: {item['email']}")

def salvar_cadastros():
    try:
        with open(arquivo_cadastros, "w") as arquivo:
            for cadastro in lista:
                arquivo.write(f"{cadastro['nome']},{cadastro['email']}\n")
    except Exception as e:
        messagebox.showerror("Erro ao salvar", f"Não foi possível salvar os cadastros: {e}")

def carregar_cadastros():
    global lista
    lista = []
    if os.path.exists(arquivo_cadastros):
        try:
            with open(arquivo_cadastros, "r") as arquivo:
                for linha in arquivo:
                    nome, email = linha.strip().split(",")
                    lista.append({"nome": nome, "email": email})
        except Exception as e:
            messagebox.showerror("Erro ao carregar", f"Não foi possível carregar os cadastros: {e}")
    atualizar_lista()

def voltar_para_principal():
    janela.destroy()

def excluir_cadastro():
    global lista
    try:
        indice_selecionado = lista_cadastros_listbox.curselection()[0]
        cadastro_selecionado = lista[indice_selecionado]
        confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir o cadastro de {cadastro_selecionado['nome']}?")
        if confirmacao:
            del lista[indice_selecionado]
            salvar_cadastros() 
            atualizar_lista()
    except IndexError:
        messagebox.showerror("Erro", "Selecione um cadastro para excluir.")

def editar_cadastro():
    global indice_editando, janela_edicao, entrada_nome_edicao, entrada_email_edicao
    try:
        indice_selecionado = lista_cadastros_listbox.curselection()[0]
        cadastro_selecionado = lista[indice_selecionado]
        indice_editando = indice_selecionado

        janela_edicao = tk.Toplevel(janela)
        janela_edicao.title("Editar Cadastro")

        rotulo_nome_edicao = tk.Label(janela_edicao, text="Nome:", font=("Arial", 12))
        rotulo_nome_edicao.pack(pady=5)
        entrada_nome_edicao = tk.Entry(janela_edicao, width=20, font=("Arial", 14))
        entrada_nome_edicao.insert(tk.END, cadastro_selecionado['nome'])
        entrada_nome_edicao.pack(pady=5)

        rotulo_email_edicao = tk.Label(janela_edicao, text="Email:", font=("Arial", 12))
        rotulo_email_edicao.pack(pady=5)
        entrada_email_edicao = tk.Entry(janela_edicao, width=20, font=("Arial", 14))
        entrada_email_edicao.insert(tk.END, cadastro_selecionado['email'])
        entrada_email_edicao.pack(pady=5)

        botao_salvar_edicao = tk.Button(janela_edicao, text="Salvar Edição", command=salvar_edicao)
        botao_salvar_edicao.pack(pady=10)

    except IndexError:
        messagebox.showerror("Erro", "Selecione um cadastro para editar.")

def salvar_edicao():
    global indice_editando
    try:
        with open(arquivo_cadastros, "w") as arquivo:
            for cadastro in lista:
                arquivo.write(f"{cadastro['nome']},{cadastro['email']}\n")
    except Exception as e:
        messagebox.showerror("Erro ao salvar", f"Não foi possível salvar os cadastros: {e}")
    if indice_editando is not None and hasattr(janela_edicao, 'destroy'):
        novo_nome = entrada_nome_edicao.get()
        novo_email = entrada_email_edicao.get()
        if novo_nome and novo_email:
            lista[indice_editando]['nome'] = novo_nome
            lista[indice_editando]['email'] = novo_email
            salvar_cadastros() 
            atualizar_lista()
            janela_edicao.destroy()
            indice_editando = None
            messagebox.showinfo("Sucesso", "Cadastro editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showerror("Erro", "Nenhum cadastro em edição.")

janela = tk.Tk()
janela.title("Cadastros Realizados")
janela.geometry("400x500")
janela.configure(bg="#cccccc")

rotulo_lista = tk.Label(janela, bg="#cccccc", text="Cadastro Realizados", font=("Forte", 24))
rotulo_lista.pack(pady=5)

lista_cadastros_listbox = tk.Listbox(janela, width=40, height=15, font=("Arial", 12))
lista_cadastros_listbox.pack(pady=10)

btn_frame = tk.Frame(janela, bg="#cccccc")
btn_frame.pack(pady=0)

botao_excluir_cadastro = tk.Button(btn_frame, text="Excluir Selecionado", bg="#ff5252", width=15, height=2, command=excluir_cadastro)
botao_excluir_cadastro.pack(pady=10, padx=5, side="left")
botao_editar_cadastro = tk.Button(btn_frame, text="Editar Selecionado", bg="#6fff52", width=15, height=2, command=editar_cadastro)
botao_editar_cadastro.pack(pady=10, padx=5, side="left")
botao_voltar = tk.Button(btn_frame, text="Voltar", bg="#52ceff", width=15, height=2, command=voltar_para_principal)
botao_voltar.pack(pady=10, padx=5, side="left")

carregar_cadastros()
janela.mainloop()
