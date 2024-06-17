#feito por Eduardo Pedroso
#https://github.com/EP3droso

# main.py
from banda import Banda
from musico import Musico
from album import Album
from menu import Menu
from instrumento import Guitarra, Bateria

# Criando instrumentos
guitarra = Guitarra('Fender Stratocaster', 'Cordas', 6)
bateria = Bateria('Yamaha Stage Custom', 'Percussão', 5)
# Criando músicos com instrumentos
musico1 = Musico('John', guitarra)
musico2 = Musico('Ringo', bateria)
# Criando banda e adicionando músicos
banda = Banda('The Beatles')
banda.adicionar_musico(musico1)
banda.adicionar_musico(musico2)
#criar album
album1 = Album('The Beatles(The White Album)','1968','"Back in the U.S.S.R.", "Dear Prudence", "Glass Onion", "Ob-La-Di, Ob-La-Da", "Wild Honey Pie", "The Continuing Story of Bungalow Bill", "While My Guitar Gently Weeps", "Happiness Is a Warm Gun", "Martha My Dear", "Im So Tired", "Blackbird", "Piggies", "Rocky Raccoon", "Dont Pass Me By", "Why Dont We Do It in the Road?", "I Will", "Julia", "Birthday", "Yer Blues", "Mother Natures Son", "Everybodys Got Something to Hide Except Me and My Monkey", "Sexy Sadie", "Helter Skelter", "Long, Long, Long", "Revolution 1", "Honey Pie", "Savoy Truffle", "Cry Baby Cry", "Revolution 9", "Good Night"')

#adicionar album
banda.adicionar_album(album1)


# Exibindo informações da banda
menu1 = Menu('0',True,banda)

while(menu1.varFechar):
    menu1.rodar()
    
    