import tkinter as tk

janela = tk.Tk()
janela.title = ("Lista de Cadastro")
janela.geometry = ("Cadastro")
janela.configure = ("300x400")

janela_cadastro = tk.Button(text="Realizar cadastro")
janela_cadastro.pack(pady=10)

janela.mainloop()