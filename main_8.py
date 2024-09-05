from classes_3 import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_enderecos('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Stephany', 20)
cliente2.inserir_enderecos('Goiânia', 'GO')
print(cliente2.nome)
cliente2.lista_enderecos()
print()


cliente3 = Cliente('Nathália', 21)
cliente3.inserir_enderecos('Rio de Janeiro', 'RJ')
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('##################')


