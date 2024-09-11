from contato_1 import  Contato1

class Agenda1:
    def __init__(self):
        self.contatos = []
    
    def armazenar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato de {contato.nome} armazenado!")
    
    def remover_contato(self, contato):
        if contato in self.contatos:
            self.contatos.remove(contato)
            print(f"Contato de {contato.nome} removido")
        else:
            print("Este contato não existe")
    
    def busca_contato(self, nome):
        for i, contato in enumerate(self.contatos):
            if contato.nome.lower() == nome.lower():
                print(f"Contato encontrado na posição {i}")
                
    
    def imprimir_agenda(self):
        if not self.contatos:
            print("Não há contatos salvos ainda.")
        else:
            for contato in self.contatos:
                contato.imprimir_dados()
    
    def imprimir_contato(self, index):
        if 0 <= index < len(self.contatos):
            self.contatos[index].imprimir_dados()
        else:
            print("Índice inválido.")

            

