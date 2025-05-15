import tkinter as tk
import subprocess

arquivo_cadastros = "cadastros.txt"

janela = tk.Tk()
janela.title("Pagina Principal")
janela.geometry("300x200")
janela.configure(bg="#cccccc")

def abrir_Tela2():
    subprocess.Popen(["python", "Tela2.py"])

def abrir_Tela3():
    subprocess.Popen(["python", "Tela3.py"])

janelaf = tk.Frame(janela, bg="#cccccc")
janelaf.pack(pady=18)

janela_fcadastro = tk.Button(text="Realizar cadastro", bg="#52ffcb", width=18, height=1, font=("MS Serif", 18), command= abrir_Tela2)
janela_fcadastro.pack(pady=5)

janela_visualizarc = tk.Button(text="Visualizar Cadastros",bg="#52fffc", width=18, height=1, font=("MS Serif", 18), command= abrir_Tela3)
janela_visualizarc.pack(pady=10)
janela.mainloop()