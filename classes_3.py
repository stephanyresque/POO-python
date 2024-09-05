#Composição: Uma classe vai ser dona de objetos de outra classe
#Se a classe principal for apagada todos os objetos da outra classe tbm será

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
    
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FORAM APAGADOS')

#__del__ apaga ao final da execução, mas caso você apague na main, ele executa antes para o objeto que você apagou.