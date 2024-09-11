#Encapsulamento -> esconder certas partes do código -> mais segurança

"""
public (métodos e atributos que podem ser acessados dentro ou fora da classe)
, protect(acessados apenas dentro da classe ou das filhas daquela classe), 
private (só está disponível dentro da classe).

"_": protect
"__": private 

"""

class BasedeDados:
    def __init__(self): #construtor!
        self.__dados = {}

    @property #assim eu libero como publico
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})
    
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]

    


bd = BasedeDados()

bd.inserir_cliente(1, 'Stephany')
bd.inserir_cliente(2, 'Antônio')
bd.inserir_cliente(3, 'Adriano')
bd.inserir_cliente(4, 'Miguel')

print(bd.dados)
print()
bd.lista_clientes()
print()
bd.apaga_clientes(3)
print(bd.dados)

"""
bd.__dados = 'outra coisa' #por ser privado, não quebrou -> criou um outro atributo
print(bd.__dados)
print(bd._BasedeDados__dados)
bd.lista_clientes()
"""
"""
bd.inserir_cliente(1, 'Stephany')
bd.inserir_cliente(2, 'Antônio')
bd.inserir_cliente(3, 'Adriano')

print(bd.dados)

bd.apaga_clientes(3)
print(bd.dados)
bd.lista_clientes()
"""