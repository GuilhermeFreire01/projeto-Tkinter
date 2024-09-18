import tkinter as tk

class Janela:
    def visualizar_janela(self):
        janela = tk.Tk()
        janela.title ("Primeira Janela")
        janela.geometry("300x200")

        janela.mainloop()
