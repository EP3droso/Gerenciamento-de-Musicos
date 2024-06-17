from instrumento import Instrumento
class Musico:
    def __init__(self, nome, instrumento: Instrumento):
       self.nome = nome
       self.instrumento = instrumento
       
    def mostrar_info(self):
        print(f'Músico: {self.nome}')
        self.instrumento.mostrar_info()
