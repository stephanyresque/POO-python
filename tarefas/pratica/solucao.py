from abc import ABC, abstractmethod
import random

# Interface FuncionarioAssalariado
class FuncionarioAssalariado(ABC):
    @abstractmethod
    def receberSalario(self, nTurmas: int):
        pass

# Classe Professor
class Professor(FuncionarioAssalariado):
    def __init__(self, nome: str, nTurmas: int, salario: float):
        self._nome = nome
        self._nTurmas = nTurmas
        self._salario = salario

    def elaborarProvas(self) -> list:
        # Lógica para elaborar provas: cria 3 questões por turma
        questoes = []
        for i in range(self._nTurmas):
            questoes.append(f"Questão da Turma {i+1}")
        return questoes

    def corrigirProva(self, prova):
        # Lógica para corrigir prova: calcula nota aleatória para simplificação
        nota = random.uniform(0, 10)  # Nota entre 0 e 10
        prova.setNota(nota)
        return nota

    def getNome(self) -> str:
        return self._nome

    def setNome(self, nome: str):
        self._nome = nome

    def getnTurmas(self) -> int:
        return self._nTurmas

    def setnTurmas(self, nTurmas: int):
        self._nTurmas = nTurmas

    def getSalario(self) -> float:
        return self._salario

    def setSalario(self, salario: float):
        self._salario = salario

    def estudar(self):
        # Lógica para estudar (método vazio, já que o Professor não estuda)
        pass

    def receberSalario(self, nTurmas: int):
        # Aumenta o salário baseado no número de turmas
        self._salario += nTurmas * 100  
        return self._salario

# Classe ProfessorUniversitario
class ProfessorUniversitario(Professor):
    def __init__(self, nome: str, nTurmas: int, salario: float):
        super().__init__(nome, nTurmas, salario)

    def elaborarProvas(self) -> list:
        # Lógica específica para elaborar provas universitárias
        questoes = super().elaborarProvas()
        questoes.append("Questão adicional de nível universitário")
        return questoes

# Classe Aluno
class Aluno:
    def __init__(self, nome: str, nMatricula: int):
        self._nome = nome
        self._nMatricula = nMatricula

    def fazerProva(self, prova):
        # Simula a entrega de respostas aleatórias para a prova
        respostas = [random.choice(["A", "B", "C", "D"]) for _ in prova.getQuestoes()]
        prova.setRespostas(respostas)

    def getNome(self) -> str:
        return self._nome

    def setNome(self, nome: str):
        self._nome = nome

    def getnMatricula(self) -> int:
        return self._nMatricula

    def setnMatricula(self, nMatricula: int):
        self._nMatricula = nMatricula

    def estudar(self):
        # Lógica para estudar
        print(f"{self._nome} está estudando.")

# Classe Prova
class Prova:
    def __init__(self, questoes: list):
        self._questoes = questoes
        self._respostas = []
        self._nota = 0.0

    def getQuestoes(self) -> list:
        return self._questoes

    def setRespostas(self, respostas: list):
        self._respostas = respostas

    def getRespostas(self) -> list:
        return self._respostas

    def setQuestoes(self, questoes: list):
        self._questoes = questoes

    def getNota(self) -> float:
        return self._nota

    def setNota(self, nota: float):
        self._nota = nota

# Classe para testar a solução
class TestaSolucao:
    @staticmethod
    def main():
        # Criação de um professor universitário
        professor = ProfessorUniversitario("Dr. Silva", 3, 3000)
        print(f"Professor: {professor.getNome()}, Salário: {professor.getSalario()}")

        # Elaborar prova
        questoes = professor.elaborarProvas()
        prova = Prova(questoes)
        print(f"Questões elaboradas: {prova.getQuestoes()}")

        # Criar um aluno e fazer a prova
        aluno = Aluno("João", 12345)
        aluno.fazerProva(prova)
        print(f"Respostas do aluno: {prova.getRespostas()}")

        # Corrigir a prova
        nota = professor.corrigirProva(prova)
        print(f"Nota da prova: {nota}")

        # Receber salário
        novo_salario = professor.receberSalario(professor.getnTurmas())
        print(f"Novo Salário: {novo_salario}")

# Chama o método main para executar
if __name__ == "__main__":
    TestaSolucao.main()
