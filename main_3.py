from produto import Produto

p1 = Produto('SAPATO', 250)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CAneCa', 'R$15') #getter e setter resolvem este problema
p2.desconto(10)
print(p2.nome, p2.preco)