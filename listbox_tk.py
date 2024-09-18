import tkinter as tk

class Listbox():
    def visualizar_listbox(self):

        def mostrar_selecao():
            selecao = lista.curselection()
            print("Item selecionado: ", lista.get(selecao))

        janela = tk.Tk()
        janela.title("Exemplo de lista")
        lista = tk.Listbox(janela)
        lista.insert(1, "Opção 1")
        lista.insert(2, "Opção 2")
        lista.insert(3, "Opção 3")
        lista.pack(pady=10)
        botao = tk.Button(janela, text="Mostrar Seleção",
                        command=mostrar_selecao)
        botao.pack(pady=10)
        janela.mainloop()