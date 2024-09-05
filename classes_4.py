"""
Associação - Usa | Agregação - Tem | Composição - É dono | 
Herança - É
"""

#Herança: um objeto é outro objeto

class Pessoa: #Super Classe
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeClasse} está falando...')

class Cliente(Pessoa): #herda da classe Pessoa -> Sub classe
    def comprar(self):
        print(f'{self.nomeClasse} está comprando...')

class Aluno(Pessoa): # Sub classe
    def estudar(self):
        print(f'{self.nomeClasse} está estudando...')

