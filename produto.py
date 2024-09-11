#Getters e Setters

#getter "mostra" o valor e setter configura um valor
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    #getter -> é chamado quando faço "self.preco"
    @property #outro decorador
    def preco(self): #repare que é o mesmo nome do atributo
        return self._preco
    
    #Setter -> vai ser chamado ainda no __init__ quando atribuo algum valor "self.preco = preco"
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

#OBS: Getter e Setter são como filtros; podem ser chamados dentro de funções