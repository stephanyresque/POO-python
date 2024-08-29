from datetime import datetime
from random import randint

#método da classe é como a variável da classe. É uma função disponível a toda classe. Uma função(método) que se baseia na classe.
#métodos estáticos: não precisa nem de uma instância (self) nem da classe (cls)
class Pessoa: 

    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) 

    def __init__(self, name, old, comendo=False, falando=False):
        self.nome = name   
        self.idade = old
        self.comendo = comendo     
        self.falando = falando
    
    def falar(self, assunto): #aqui temos um método que se baseia na instância
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto come!')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} está falando agora.')
            return
        
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
    
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    
    def ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod #acabei de criar um método(função) que se baseia na classe.
    def por_ano_nascimento(cls, nome, ano_nascimento): #"cls" refere-se a  classe "Pessoa", assim como "self" se refere a instância
        idade = cls.ano_atual - ano_nascimento #veja que a variável global da classe está disponível
        return cls(nome, idade) #assim eu consigo criar uma nova instância
    
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand
        

"""
OBS: "@classmethod" é um decorador que decora um método de classe
OBS: "staticmethod" tbm é um decorador
"""
