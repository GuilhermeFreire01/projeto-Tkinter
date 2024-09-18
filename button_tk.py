import tkinter as tk

def on_button_click():
    print("Botão clicado!")

root = tk.Tk()
root.title("Exemplo de Tela com Botão")

root.geometry("300x200")

button = tk.Button(root, text="Clique Aqui", command=on_button_click)
button.pack(pady=20)

root.mainloop()
