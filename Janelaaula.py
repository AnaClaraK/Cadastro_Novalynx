import tkinter as tk

#criar função para add os itens na lista

lista = []

def adicionar_item():
    item = entrada.get()
    if item:
        lista.append(item)  
        entrada.delete(0, tk.END)     #Limpar campo de entrada
        atualizar_lista()

#função para atualizar lista
def atualizar_lista():
    texto_lista = "\n" .join(f"{i}-{item}" for i, item in enumerate(lista)) if lista else "nenhum item adicionado" #posições
    rotulo_lista.config(text=texto_lista)

janela = tk.Tk()
janela.title("Lista de Compras")
janela.geometry("400x500")
janela.configure(bg="#aadfe6")

rotulo = tk.Label(janela, bg ="#aadfe6", text="Digite um Item", font=("Forte", 20))
rotulo.pack(pady=10)

entrada = tk.Entry(janela, width=15, font=("Arial", 20))
entrada.pack(pady=10)
btn_adicionar = tk.Button(janela, text= "Adicionar", command = adicionar_item)
btn_adicionar.pack(pady=10, anchor= "e", padx=20)

rotulo_lista = tk.Label(janela, text ="", width=20, height=20, anchor = "nw", justify=tk.LEFT, font = ("Arial", 20), relief = "solid")
rotulo_lista.pack(pady=10) 

janela.mainloop()