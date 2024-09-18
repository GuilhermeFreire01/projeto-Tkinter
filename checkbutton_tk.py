import tkinter as tk
class Checkbutton():
    def visualizar_checkbutton(self):
        def verificar():
            if opcao.get():
                print("Selecionado")
            else:
                print("Não selecionado")

        janela = tk.Tk()
        janela.title("Exemplo simples de checkbutton")
        opcao = tk.IntVar()
        check = tk.Checkbutton(janela, text="Escolha esta opção",
                            variable=opcao, command=verificar)
        check.pack(pady=10)
        janela.mainloop()