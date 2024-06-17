class Album:
    def __init__(self, titulo, ano,lista_de_faixas):
        self.titulo= titulo
        self.ano = ano
        self.lista_de_faixas = lista_de_faixas

    def mostrar_info(self):
        print('Album: ')
        print(f'Título: {self.titulo}, Ano: {self.ano}, Lista de Faixas: {self.lista_de_faixas}')
