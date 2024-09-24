from abc import ABC, abstractmethod

class FuncionarioAssalariado(ABC):
    
    @abstractmethod
    def receberSalario(self, nTurmas: int) -> None:
        pass

class Professor(FuncionarioAssalariado):
    
    def __init__(self, nome: str, nTurmas: int, salario: float):
        self.nome = nome
        self.nTurmas = nTurmas
        self.salario = salario

    def receberSalario(self, nTurmas: int) -> None:
        self.salario = nTurmas * (self.salario / self.nTurmas)
        print(f"O salário do professor {self.nome} é: R${self.salario:.2f}")

    
prof = Professor("João", 5, 3000.0)
prof.receberSalario(5)
