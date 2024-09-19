import tkinter as tk

class Radiobutton():
    def visualizar_radiobutton(self):
        def mostrar_opcao():
            print(f"Opção selecionada: {opcao.get()}")
        janela = tk.Tk()
        janela.title("Exemplo de Radiobutton")
        opcao = tk.StringVar(value="Opcao 1")
        radio1 = tk.Radiobutton(janela, text="Opção 1",
                                variable=opcao, value="Opção 1",
                                command=mostrar_opcao)
        radio1.pack()
        radio2 = tk.Radiobutton(janela, text="Opção 2",
                                variable=opcao, value="Opção 2",
                                command=mostrar_opcao)
        radio2.pack()
        janela.mainloop()

