from pessoa_2 import Pessoa

#p1 = Pessoa.por_ano_nascimento('Stephany', 2003)

p1 = Pessoa('Stephany', 21)


print(p1)
print(p1.nome, p1.idade)
print(p1.ano_nascimento())
print(Pessoa.gera_id()) #é possível chamar este método por uma instância "p1.gera_id()"