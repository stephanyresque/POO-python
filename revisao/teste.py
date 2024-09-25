from modelo import *

prof01 = ProfessorEducacaoBasica('João', 5, 1500)
prof02 = ProfessorUniversitario('Amanda', 10, 2500)
aluno01 = Aluno('Stephany', 202400316)

prova01 = prof01.elaborarProvas()
prova02 = prof02.elaborarProvas()

aluno01.fazerProva(prova01)


print(prof01.corrigirProvas(prova01))



