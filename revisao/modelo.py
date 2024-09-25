from abc import ABC, abstractmethod

class Professor(ABC):

    def __init__(self, nome, nTurmas, salario):
        self.__nome = nome
        self.__nTurmas = nTurmas
        self.__salario = salario
    
    @abstractmethod
    def elaborarProvas(self) -> list:
        pass

    @abstractmethod
    def corrigirProvas(self, prova) -> float:
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
        provas = []
        for _ in range(self.nTurmas):
            questoes = [f"{j+1}" for j in range(5)] 
            prova = Prova(questoes)
            provas.append(prova)
        return provas

class ProfessorUniversitario(Professor):
    
    def elaborarProvas(self):
        provas = []
        for _ in range(self.nTurmas):
            questoes = [f"{j+1}" for j in range(10)]  
            prova = Prova(questoes)
            provas.append(prova)
        return provas
    
    def corrigirProvas(self, prova):
        nota_total = 0
        for i, resposta in enumerate(prova.respostas):
            if resposta == "resposta correta": 
                nota_total += 1
        prova.nota(nota_total)
        return nota_total
    
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
        self.respostas = []

    def fazerProva(self, prova):
        for i in range(len(prova.questoes)):
            resp = input(f"Digite a {i+1}° resposta do aluno")
            self.respostas.append(resp)
        
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

    

