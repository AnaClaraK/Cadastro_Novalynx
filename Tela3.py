import tkinter as tk

#criar função para add os itens na lista

lista = []
#Funções
def atualizar_lista():
    texto_lista = "\n" .join(f"{i}-{item}" for i, item in enumerate(lista)) if lista else "nenhum item adicionado" #posições
    rotulo_lista.config(text=texto_lista)

def voltar_para_principal():
    """Volta para a tela principal e esconde a tela atual."""
    janela_atual = janela_cadastro if janela_cadastro.winfo_ismapped() else janela_visualizacao
    janela_atual.withdraw()
    janela_principal.deiconify()

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

janela = tk.Tk()
janela.title("Cadastros Realizados")
janela.geometry("400x500")
janela.configure(bg="#aadfe6")

rotulo = tk.Label(janela, bg ="#aadfe6", text="Cadastro Realizados", font=("Forte", 20))
rotulo.pack(pady=10)

rotulo_lista = tk.Label(janela, text ="", width=20, height=20, anchor = "nw", font = ("Arial", 20), relief = "solid")
rotulo_lista.pack(pady=10) 

lista_cadastros_listbox = tk.Listbox(janela, width=50, height=15, font=("Arial", 12))
lista_cadastros_listbox.pack(pady=10)

botao_excluir_cadastro = tk.Button(janela, text="Excluir Selecionado", command=excluir_cadastro)
botao_excluir_cadastro.pack(pady=5)
botao_editar_cadastro = tk.Button(janela, text="Editar Selecionado", command=editar_cadastro)
botao_editar_cadastro.pack(pady=5)
botao_voltar = tk.Button(janela, text="Voltar", command=voltar_para_principal)
botao_voltar.pack(pady=5)

janela.mainloop()