#Permita adicionar e remover músicos e álbuns dinamicamente.
#Implemente uma interface simples no console para interagir com o sistema.

from musico import Musico
from album import Album
from banda import Banda
from instrumento import Instrumento
from instrumento import Guitarra
from instrumento import Bateria
from album import Album



class Menu:
    def __init__(self, estado, varFechar, novaBanda):
        self.estado = estado
        self.varFechar = varFechar
        self.novaBanda = novaBanda



    def rodar(self):
        if(self.estado == '0'):
            print('''=============================
      Gerenciamento de Banda
=============================
0. Fechar
1. Membros
2. Albúns

=============================
''')

            resposta = str(input('Escolha uma opção: '))
            resposta = str(resposta)
            if(resposta == '0'):
                self.varFechar = False
                
            self.estado = resposta
            

        elif(self.estado == '1'):
            print('''=============================
      Membros
=============================
0. Voltar para o menu
1. Vizualizar Membros
2. Adicionar Membros
3. Remover Membros


=============================
''')
            resposta = str(input('Escolha uma opção: '))

            if(resposta == '0'):
                self.estado = '0'

        
            elif(resposta == '1'):
                self.novaBanda.mostrar_musicos()

            elif(resposta == '2'):
                nome = str(input("nome: "))
                tipoInstrumento = str(input("Tipo do instrumento: "))

                if(tipoInstrumento == 'cordas' or tipoInstrumento == "Cordas"):
                    nomeInstrumento = str(input("Nome do Instrumento: "))
                    numeroCordas = str(input("Numero de Cordas: "))

                    novoInstrumento = Guitarra(nomeInstrumento,tipoInstrumento,numeroCordas)

                elif(tipoInstrumento == 'percurssão' or tipoInstrumento == "Percurssão"):
                    nomeInstrumento = str(input("Nome do Instrumento: "))
                    numeroTambores = str(input("Numero de Tambores: "))

                    novoInstrumento = Bateria(nomeInstrumento,tipoInstrumento,numeroTambores)



                novoMusico = Musico(nome,novoInstrumento)

                self.novaBanda.adicionar_musico(novoMusico)
            
            elif(resposta == '3'):
                novaLista = self.novaBanda.lista_musicos()
                print(novaLista)


                index = int(input("numero do musico a ser removido: "))

                self.novaBanda.remover_musico(index)

            



        elif(self.estado == '2'):
            print('''=============================
      Albúns
=============================
0. Voltar para o menu
1. Vizualizar Albúns
2. Adicionar Albúns
3. Remover Albúns


=============================
''')
            resposta = str(input('Escolha uma opção: '))


            if(resposta == '0'):
                self.estado = '0'

            elif(resposta == '1'):
                self.novaBanda.mostrar_albuns()

            elif(resposta == '2'):
                titulo = str(input("Título do Albúm: "))
                ano = str(input("Ano de lançamento: "))
                listaDeFaixas = str(input("Lista de Faixas: "))

                novoAlbum = Album(titulo,ano,listaDeFaixas)

                self.novaBanda.adicionar_album(novoAlbum)

            elif(resposta == '3'):
                novaLista = self.novaBanda.lista_albuns()
                print(novaLista)


                index = int(input("numero do album a ser removido: "))

                self.novaBanda.remover_album(index)





        