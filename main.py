from controller_tk import Controller

class Main():
    def __init__(self) -> None:
        self.controller = Controller()
    
    def executar(self):
        self.controller.iniciar()

main = Main()
main.executar()