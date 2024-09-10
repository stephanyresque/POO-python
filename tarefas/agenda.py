from contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    # Método para armazenar um novo contato
    def armazenar_contato(self, contato):
        self.contatos.append(contato)
        print(f"{contato.nome} armazenado com sucesso!")
    
    #Método para remover contatos
    def remover_contato(self, contato):
        if contato in self.contatos:
            self.contatos.remove(contato)
            print(f"{contato.nome} foi removido da agenda.")
        else:
            print("Não há este contato na agenda.")
        
    # Método para buscar um contato pelo nome e retornar o índice
    def busca_contato(self, nome):
        for i, contato in enumerate(self.contatos):
            if contato.nome.lower() == nome.lower():
                return i
            else:
                print("Não há este contato na agenda.")
    
    def imprime_agenda(self):
        if not self.contatos:
            print("Não há contatos cadastrados na agenda.")
        else:
            for contato in self.contatos:
                contato.imprimir_dados()
                print("-------------")
    
    # Método para imprimir um contato específico pelo índice
    def imprime_contato(self, index):
        if 0 <= index < len(self.contatos):
            self.contatos[index].imprimir_dados()
        else:
            print("Índice inválido.")

# Programa principal
if __name__ == "__main__":
    # Criando instâncias de Contato
    contato1 = Contato("João Silva", "joao.silva@email.com", "12345-6789")
    contato2 = Contato("Maria Oliveira", "maria.oliveira@email.com", "98765-4321")

    # Criando uma instância de Agenda
    minha_agenda = Agenda()

    # Armazenando contatos na agenda
    minha_agenda.armazenar_contato(contato1)
    minha_agenda.armazenar_contato(contato2)

    # Imprimindo todos os contatos da agenda
    print("\nAgenda completa:")
    minha_agenda.imprime_agenda()

    # Buscando um contato pelo nome
    indice = minha_agenda.busca_contato("João Silva")
    if indice != -1:
        print(f"\nContato 'João Silva' encontrado na posição {indice}")
    else:
        print("\nContato 'João Silva' não encontrado.")

    # Imprimindo um contato específico pelo índice
    print("\nImprimindo contato na posição 0:")
    minha_agenda.imprime_contato(0)

    # Removendo um contato
    minha_agenda.remover_contato(contato1)

    # Tentando imprimir o contato removido
    print("\nTentando imprimir o contato removido:")
    minha_agenda.imprime_contato(0)

    # Imprimindo a agenda após a remoção
    print("\nAgenda após remoção:")
    minha_agenda.imprime_agenda()