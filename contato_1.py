class Contato1:
    def __init__(self, nome, email,telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
    @email.setter
    def email(self, valor):
        self.__email = valor
    
    @telefone.setter
    def telefone(self,valor):
        self.__telefone = valor

    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        
