from agenda_01 import Agenda1
from contato_1 import Contato1

contato1 = Contato1("João Silva", "joao.silva@email.com", "12345-6789")
contato2 = Contato1("Maria Oliveira", "maria.oliveira@email.com", "98765-4321")

minha_agenda = Agenda1()

minha_agenda.armazenar_contato(contato1)
minha_agenda.armazenar_contato(contato2)
print()
minha_agenda.imprimir_agenda()
print()
minha_agenda.busca_contato('Maria Oliveira')
print()
minha_agenda.imprimir_contato(0)

