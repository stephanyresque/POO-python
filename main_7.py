#Agregação
from classes_2 import Produto, CarrinhodeCompras

carrinho = CarrinhodeCompras()

#print(carrinho)

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 7000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)


carrinho.lista_produto()
print(carrinho.soma_total())