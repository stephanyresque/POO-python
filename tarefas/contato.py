
class Contato:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    #métodos getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def email(self):
        return self.__email
    
    @property
    def telefone(self):
        return self.__telefone
    
    #métodos setters
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    def imprimir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")

# Programa principal
if __name__ == "__main__":
    # Criando um objeto Contato
    contato1 = Contato("João Silva", "joao.silva@email.com", "12345-6789")
    
    # Imprimindo os dados do contato
    contato1.imprimir_dados()

    # Modificando os dados do contato utilizando os setters com @property
    contato1.nome = "Maria Oliveira"
    contato1.email = "maria.oliveira@email.com"
    contato1.telefone = "98765-4321"

    # Imprimindo os dados atualizados
    print("\nDados atualizados:")
    contato1.imprimir_dados()