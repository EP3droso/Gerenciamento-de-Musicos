# banda.py
from musico import Musico
from album import Album
class Banda:
   def __init__(self, nome):
      self.nome = nome
      self.musicos = []
      self.albuns = []


   def adicionar_musico(self, musico):
      self.musicos.append(musico)
      
   def remover_musico(self,index):
      self.musicos.pop(index)

   def mostrar_musicos(self):
      print(f'Banda: {self.nome}') 
      for musico in self.musicos: musico.mostrar_info()

   def mostrar_albuns(self):
       
      for album in self.albuns: album.mostrar_info()

   def adicionar_album(self,album):
      self.albuns.append(album)

   def remover_album(self,index):
      self.albuns.pop(index)

   def lista_musicos(self):
      lista = []
      index = 0
      for musico in self.musicos: 
         nomeLista = musico.nome
         nomeLista = str(index)+ '. ' + nomeLista
         lista.append(nomeLista)
         index +=1
      return lista
   
   def lista_albuns(self):
      lista = []
      index = 0
      for album in self.albuns: 
         nomeLista = album.titulo
         nomeLista = str(index)+ '. ' + nomeLista
         lista.append(nomeLista)
         index +=1
      return lista
   