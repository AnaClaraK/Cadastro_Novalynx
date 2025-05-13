import tkinter as tk
from tkinter import messagebox

# Lista para armazenar os dados dos cadastros
lista_cadastros = []
indice_editando = None  # Variável para rastrear o índice do cadastro sendo editado

# --- Funções Comuns ---
def atualizar_lista_cadastros():
    """Atualiza o Listbox com os cadastros."""
    lista_cadastros_listbox.delete(0, tk.END)
    for i, cadastro in enumerate(lista_cadastros):
        lista_cadastros_listbox.insert(tk.END, f"{i+1}- Nome: {cadastro['nome']}, Email: {cadastro['email']}")

def limpar_campos_cadastro():
    """Limpa os campos de entrada da janela de cadastro."""
    entrada_nome_cadastro.delete(0, tk.END)
    entrada_email_cadastro.delete(0, tk.END)

# --- Funções de Navegação ---
def abrir_tela_cadastro():
    """Abre a tela de cadastro e esconde a tela atual."""
    janela_principal.withdraw()
    janela_cadastro.deiconify()

def abrir_tela_visualizacao():
    """Abre a tela de visualização e esconde a tela atual."""
    atualizar_lista_cadastros()  # Garante que a lista esteja atualizada ao abrir
    janela_principal.withdraw()
    janela_visualizacao.deiconify()

def voltar_para_principal():
    """Volta para a tela principal e esconde a tela atual."""
    janela_atual = janela_cadastro if janela_cadastro.winfo_ismapped() else janela_visualizacao
    janela_atual.withdraw()
    janela_principal.deiconify()

# --- Funções da Tela de Cadastro (Tela 2) ---
def realizar_cadastro():
    """Realiza o cadastro, adiciona à lista e volta à tela principal."""
    global lista_cadastros
    nome = entrada_nome_cadastro.get()
    email = entrada_email_cadastro.get()

    if nome and email:
        lista_cadastros.append({"nome": nome, "email": email})
        limpar_campos_cadastro()
        voltar_para_principal()
        messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# --- Funções da Tela de Visualização (Tela 3) ---
def excluir_cadastro():
    """Exclui o cadastro selecionado."""
    global lista_cadastros, indice_editando
    try:
        indice_selecionado = lista_cadastros_listbox.curselection()[0]
        cadastro_selecionado = lista_cadastros[indice_selecionado]
        confirmacao = messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir o cadastro de {cadastro_selecionado['nome']}?")
        if confirmacao:
            del lista_cadastros[indice_selecionado]
            atualizar_lista_cadastros()
            if indice_editando == indice_selecionado:
                indice_editando = None
    except IndexError:
        messagebox.showerror("Erro", "Selecione um cadastro para excluir.")

def editar_cadastro():
    """Abre a tela de edição com os dados do cadastro selecionado."""
    global indice_editando, janela_edicao, entrada_nome_edicao, entrada_email_edicao
    try:
        indice_selecionado = lista_cadastros_listbox.curselection()[0]
        cadastro_selecionado = lista_cadastros[indice_selecionado]
        indice_editando = indice_selecionado

        janela_edicao = tk.Toplevel(janela_visualizacao)
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
    """Salva as edições feitas no cadastro."""
    global indice_editando, janela_edicao, entrada_nome_edicao, entrada_email_edicao
    if indice_editando is not None and janela_edicao:
        novo_nome = entrada_nome_edicao.get()
        novo_email = entrada_email_edicao.get()
        if novo_nome and novo_email:
            lista_cadastros[indice_editando]['nome'] = novo_nome
            lista_cadastros[indice_editando]['email'] = novo_email
            atualizar_lista_cadastros()
            janela_edicao.destroy()
            indice_editando = None
            messagebox.showinfo("Sucesso", "Cadastro editado com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        messagebox.showerror("Erro", "Nenhum cadastro em edição.")

# --- Criação das Janelas ---

# Tela 1: Janela Principal
janela_principal = tk.Tk()
janela_principal.title("Lista de Cadastro")
janela_principal.geometry("300x400")

label_principal = tk.Label(janela_principal, text="Bem-vindo!", font=("Forte", 20))
label_principal.pack(pady=20)
botao_cadastro = tk.Button(janela_principal, text="Realizar Cadastro", command=abrir_tela_cadastro)
botao_cadastro.pack(pady=10)
botao_visualizar = tk.Button(janela_principal, text="Visualizar Cadastros", command=abrir_tela_visualizacao)
botao_visualizar.pack(pady=10)

# Tela 2: Janela de Cadastro
janela_cadastro = tk.Toplevel(janela_principal)
janela_cadastro.title("Cadastro")
janela_cadastro.geometry("400x300")

rotulo_cadastro = tk.Label(janela_cadastro, text="Preencha os dados:", font=("Forte", 16))
rotulo_cadastro.pack(pady=10)

label_nome_cadastro = tk.Label(janela_cadastro, text="Nome:", font=("Arial", 12))
label_nome_cadastro.pack()
entrada_nome_cadastro = tk.Entry(janela_cadastro, width=20, font=("Arial", 14))
entrada_nome_cadastro.pack()

label_email_cadastro = tk.Label(janela_cadastro, text="Email:", font=("Arial", 12))
label_email_cadastro.pack()
entrada_email_cadastro = tk.Entry(janela_cadastro, width=20, font=("Arial", 14))
entrada_email_cadastro.pack()

botao_realizar_cadastro = tk.Button(janela_cadastro, text="Realizar Cadastro", command=realizar_cadastro) # Corrigido aqui
botao_realizar_cadastro.pack(pady=10)
botao_voltar_cadastro = tk.Button(janela_cadastro, text="Voltar", command=voltar_para_principal)
botao_voltar_cadastro.pack(pady=5)

janela_cadastro.withdraw()  # Inicia escondida

# Tela 3: Janela de Visualização
janela_visualizacao = tk.Toplevel(janela_principal)
janela_visualizacao.title("Cadastros Realizados")
janela_visualizacao.geometry("400x500")

rotulo_visualizacao = tk.Label(janela_visualizacao, text="Cadastros:", font=("Forte", 20))
rotulo_visualizacao.pack(pady=10)

lista_cadastros_listbox = tk.Listbox(janela_visualizacao, width=50, height=15, font=("Arial", 12))
lista_cadastros_listbox.pack(pady=10)

botao_excluir_cadastro = tk.Button(janela_visualizacao, text="Excluir Selecionado", command=excluir_cadastro)
botao_excluir_cadastro.pack(pady=5)
botao_editar_cadastro = tk.Button(janela_visualizacao, text="Editar Selecionado", command=editar_cadastro)
botao_editar_cadastro.pack(pady=5)
botao_voltar_visualizacao = tk.Button(janela_visualizacao, text="Voltar", command=voltar_para_principal)
botao_voltar_visualizacao.pack(pady=5)

janela_visualizacao.withdraw()  # Inicia escondida

# Iniciar a aplicação na janela principal
janela_principal.mainloop()