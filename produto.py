#Getters e Setters

#getter obtém um valor e setter configura um valor
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

    #getter -> vai ser chamado antes de passar pelo __init__
    @property #outro decorador
    def preco(self): #repare que é o mesmo nome do atributo
        return self._preco
    
    #Setter -> vai configurar o meu "preco" -> sempre que eu tentar atribuir um valor para "preco" 1° ele passa pelo setter e dps vai para o init
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

#OBS: Getter e Setter são como filtros, são chamados antes mesmo do init!