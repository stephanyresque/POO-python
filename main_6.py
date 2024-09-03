#Associação -> uma classe se associa com outra, mas não dependem uma da outra
from classes import Escritor
from classes import Caneta
from classes import MaquinadeEscrever



escritor = Escritor('Stephany')
caneta = Caneta('Bic')
maquina = MaquinadeEscrever()

escritor.ferramenta = maquina #enviando um objeto inteiro para um atributo
escritor.ferramenta.escrever() #associei 

#é como se eu jogasse toda uma classe dentro de outra, associando métodos


