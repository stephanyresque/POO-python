from abc import ABC, abstractmethod

class FuncionarioAssalariado(ABC):
    @abstractmethod
    def receberSalario(self, nTurmas):
        pass

class Estudante(ABC):
    @abstractmethod
    def estudar(self):
        pass

class Professor(ABC):

    def __init__(self, nome, nTurmas, salario):
        self.__nome = nome
        self.__nTurmas = nTurmas
        self.__salario = salario
    
    @abstractmethod
    def elaborarProvas(self):
        pass

    @abstractmethod
    def corrigirProvas(self, prova):
        pass

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nTurmas(self):
        return self.__nTurmas
    
    @nTurmas.setter
    def nTurmas(self, val):
        self.__nTurmas = val

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, val):
        self.__salario = val
    
    def estudar(self):
        print("Professor está estudando.")
    
    def receberSalario(self, nTurmas):
       salario_atual = self.__salario * nTurmas
       print(f"Salario atual do professor: R${salario_atual}")

class ProfessorEducacaoBasica(Professor):
    
    def elaborarProvas(self):
        prova = Prova(['01', '02', '03', '04', '05'])
        return prova
    
    def corrigirProvas(self, prova):
        prova.nota = 2* (len(prova.respostas))
        return prova.nota

class ProfessorUniversitario(Professor):
    
    def elaborarProvas(self):
        prova = Prova(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'])
        return prova


    def corrigirProvas(self, prova):
        prova.nota = (len(prova.respostas))
        return prova.nota
    
class Prova:
    def __init__(self, questoes:list):
        self.__questoes = questoes
        self.__respostas = []
        self.__nota = 0

    @property
    def questoes(self):
        return self.__questoes
    
    @questoes.setter
    def questoes(self, novas_questoes):
        self.__questoes = novas_questoes
    
    @property
    def respostas(self):
        return self.__respostas
    
    @respostas.setter
    def respostas(self, respostas):
        self.__respostas = respostas
        
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, nota_atribuida):
        self.__nota = nota_atribuida

    
class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def fazerProva(self, prova):
        print("Digite quantas questões o aluno respondeu: ")
        n = int(input())
        print("Digite as questões que o aluno respondeu(01, 02, 03...): ")
        for _ in range(n):
            resp = input()
            prova.respostas.append(resp)
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, val):
        self.__matricula = val

    def estudar(self):
        print("Aluno está estudando.")

