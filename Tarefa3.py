import tkinter as tk
from tkinter import messagebox
#Usar o janelaaula
lista_pessoas = []
indice_editando = None  # Variável para rastrear o índice sendo editado

def adicionar_pessoa():
    pessoa = entrada.get()
    if pessoa:
        lista_pessoas.append(pessoa)
        atualizar_listbox()
        entrada.delete(0, tk.END)

def excluir_pessoa():
    global indice_editando
    try:
        indice_selecionado = lista_cadastro.curselection()[0]
        pessoa_selecionada = lista_cadastro.get(indice_selecionado).split("-", 1)[1].strip()
        confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir '{pessoa_selecionada}'?")
        if confirmacao:
            del lista_pessoas[indice_selecionado]
            atualizar_listbox()
            if indice_editando == indice_selecionado:
                indice_editando = None
            elif indice_editando > indice_selecionado:
                indice_editando -= 1
    except IndexError:
        messagebox.showerror("Erro", "Selecione uma pessoa para excluir.")

def editar_pessoa():#N~sao fucniona
    global indice_editando
    try:
        indice_selecionado = lista_cadastro.curselection()[0]
        pessoa_selecionada = lista_cadastro.get(indice_selecionado).split("-", 1)[1].strip()
        entrada_edicao.delete(0, tk.END)
        entrada_edicao.insert(tk.END, pessoa_selecionada)
        indice_editando = indice_selecionado  # Armazena o índice globalmente
    except IndexError:
        messagebox.showerror("Erro", "Selecione uma pessoa para editar.")

def salvar_edicao():
    global indice_editando
    if indice_editando is not None:
        nova_pessoa = entrada_edicao.get()
        if nova_pessoa:
            lista_pessoas[indice_editando] = nova_pessoa
            atualizar_listbox()
            entrada_edicao.delete(0, tk.END)
            indice_editando = None  # Limpa o índice de edição
        else:
            messagebox.showerror("Erro", "O nome não pode estar vazio.")
    else:
        messagebox.showerror("Erro", "Nenhuma pessoa em edição.")

def atualizar_listbox():
    lista_cadastro.delete(0, tk.END)
    for i, pessoa in enumerate(lista_pessoas):
        lista_cadastro.insert(tk.END, f"{i+1}- {pessoa}")

janela = tk.Tk()
janela.title("Lista de Cadastro")
janela.geometry("400x500")
janela.configure(bg="#aadfe6")

rotulo = tk.Label(janela, bg="#aadfe6", text="Digite uma pessoa", font=("Forte", 20))
rotulo.pack(pady=10)

entrada = tk.Entry(janela, width=15, font=("Arial", 20))
entrada.pack(pady=10)

btn_adicionar = tk.Button(janela, text="Adicionar", command=adicionar_pessoa)
btn_adicionar.pack(pady=10, anchor="e", padx=20)

lista_cadastro = tk.Listbox(janela, width=30, height=10, font=("Arial", 16))
lista_cadastro.pack(pady=10)

btn_excluir = tk.Button(janela, text="Excluir Selecionado", command=excluir_pessoa)
btn_excluir.pack(pady=5)

btn_editar = tk.Button(janela, text="Editar Selecionado", command=editar_pessoa)
btn_editar.pack(pady=5)

entrada_edicao = tk.Entry(janela, width=15, font=("Arial", 20))
entrada_edicao.pack(pady=5)

btn_salvar = tk.Button(janela, text="Salvar Edição", command=salvar_edicao)
btn_salvar.pack(pady=5)

atualizar_listbox()

janela.mainloop()