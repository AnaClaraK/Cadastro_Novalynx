import tkinter as tk

def abrir_cadastro():
    janela_principal.withdraw()  # Torna a janela principal invisível
    janela_cadastro.deiconify() # Torna a janela de cadastro visível

def voltar_para_principal():
    janela_cadastro.withdraw()  # Torna a janela de cadastro invisível
    janela_principal.deiconify() # Torna a janela principal visível

def realizar_cadastro_acao():
    # Aqui você colocaria a lógica para salvar os dados do cadastro
    nome = entrada_nome.get()
    email = entrada_email.get()
    print(f"Cadastro realizado para: Nome={nome}, Email={email}")
    voltar_para_principal() # Volta para a janela principal após o cadastro

# --- Criação da Janela Principal ---
janela_principal = tk.Tk()
janela_principal.title("Janela Principal")
label_principal = tk.Label(janela_principal, text="Bem-vindo à Janela Principal!")
label_principal.pack(pady=20)
botao_cadastro = tk.Button(janela_principal, text="Realizar Cadastro", command=abrir_cadastro)
botao_cadastro.pack(pady=10)

# --- Criação da Janela de Cadastro ---
janela_cadastro = tk.Toplevel(janela_principal) # Tornamos a janela de cadastro filha da principal
janela_cadastro.title("Janela de Cadastro")
label_cadastro = tk.Label(janela_cadastro, text="Preencha os dados para cadastro:")
label_cadastro.pack(pady=10)

label_nome = tk.Label(janela_cadastro, text="Nome:")
label_nome.pack()
entrada_nome = tk.Entry(janela_cadastro)
entrada_nome.pack()

label_email = tk.Label(janela_cadastro, text="Email:")
label_email.pack()
entrada_email = tk.Entry(janela_cadastro)
entrada_email.pack()

botao_realizar_cadastro = tk.Button(janela_cadastro, text="Realizar Cadastro", command=realizar_cadastro_acao)
botao_realizar_cadastro.pack(pady=10)

botao_voltar = tk.Button(janela_cadastro, text="Voltar", command=voltar_para_principal)
botao_voltar.pack(pady=5)

janela_cadastro.withdraw() # Inicialmente, a janela de cadastro fica escondida

janela_principal.mainloop()