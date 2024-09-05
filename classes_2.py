#Agregação -> outra classe usa outra classe como parte de si -> elas dependem uma da outra
#As classes existem de forma INdependente, mas elas são dependentes para funcionar.

class CarrinhodeCompras:
    def __init__(self):
        self.produtos = []
    
    def inserir_produto(self, produto):
        self.produtos.append(produto)
    
    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

