import tkinter as tk
import subprocess
#FUNCIONA
janela = tk.Tk()
janela.title("Pagina Principal")
janela.geometry("200x100")

def abrir_Tela2():
    subprocess.Popen(["python", "Tela2.py"])

def abrir_Tela3():
    subprocess.Popen(["python", "Tela3.py"])

janela_fcadastro = tk.Button(text="Realizar cadastro", command= abrir_Tela2)
janela_fcadastro.pack(pady=5)

janela_visualizarc = tk.Button(text="Visualizar Cadastros", command= abrir_Tela3)
janela_visualizarc.pack(pady=10)
janela.mainloop()