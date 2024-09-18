from button_tk import Botao
from checkbutton_tk import Checkbutton
from entrada_tk import Entry
from janela_tk import Janela
from label_tk import Label
from listbox_tk import Listbox
from radiobutton_tk import Radiobutton
from textbot_tk import Textbox

class Controller():
    def __init__(self) -> None:
        self.button = Botao()
    
    def iniciar(self):
        self.button.visualizar_botao()