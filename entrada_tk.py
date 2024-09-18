import tkinter as tk
class Entry():
    def visualizar_entry():
        janela = tk.Tk()
        janela.title("Exemplo simples de entrada")

        entrada = tk.Entry(janela)
        entrada.pack(pady=10)

        janela.mainloop()
