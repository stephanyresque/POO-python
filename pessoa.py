from datetime import datetime

#nossa classe é como um molde para criar objetos/instâncias
#método da classe -> uma função que pertencente a nossa classe
#self referencia a própria instância que está chamando -> 'p1.funcao(p1)'
class Pessoa: 

    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #"ano_atual" é uma variável da classe em si -> todos os objetos da classe terão essa variável

    def __init__(self, name, old, comendo=False, falando=False): #construtor!
        self.nome = name   #esses 'self.algo' estão disponíveis para outros métodos dentro da classe 
        self.idade = old
        self.comendo = comendo     #aqui temos variáveis da instância
        self.falando = falando
    
    def falar(self, assunto):
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



#com __init__ nós "forçamos" que todas as instâncias criadas tenham os atributos name, old...
#__init__ se inicia/executa sempre que chamamos a classe 