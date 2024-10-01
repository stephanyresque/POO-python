from abc import ABC, abstractmethod

class FuncionarioAssalariado(ABC):
    """
    classe abstrata que representa um funcionário assalariado
    """
    @abstractmethod
    def receberSalario(self, nTurmas):
        """
        Método abstrato que calcula o salário com base no número de turmas.
        
        :param nTurmas: Número de turmas atribuídas ao funcionário.
        """
        pass

class Estudante(ABC):
    """
    classe abstrata que representa um estudante
    """
    @abstractmethod
    def estudar(self):
        """
        método abstrato que define a ação de estudar.
        """
        pass

class Professor(ABC):
    """
    Classe abstrata que representa um professor, derivada de FuncionarioAssalariado.
    """
    def __init__(self, nome, nTurmas, salario):
        """
        Inicializa um professor com nome, número de turmas e salário base.

        :param nome: Nome do professor.
        :param nTurmas: Número de turmas do professor.
        :param salario: Salário base do professor.
        """
        self.__nome = nome
        self.__nTurmas = nTurmas
        self.__salario = salario
    
    @abstractmethod
    def elaborarProvas(self):
        """
        Método abstrato que define a criação de provas pelo professor.
        """
        pass

    @abstractmethod
    def corrigirProvas(self, prova):
        """
        Método abstrato que define a correção de provas.

        :param prova: Objeto do tipo Prova que será corrigido.
        """
        pass

    @property
    def nome(self):
        """
        Propriedade que retorna o nome do professor.
        """
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """
        Altera o nome do professor.
        
        :param nome: Novo nome do professor.
        """
        self.__nome = nome

    @property
    def nTurmas(self):
        """
        Propriedade que retorna o número de turmas atribuídas ao professor.
        """
        return self.__nTurmas
    
    @nTurmas.setter
    def nTurmas(self, val):
        """
        Altera o número de turmas do professor.
        
        :param val: Novo número de turmas.
        """
        self.__nTurmas = val

    @property
    def salario(self):
        """
        Propriedade que retorna o salário base do professor.
        """
        return self.__salario
    
    @salario.setter
    def salario(self, val):
        """
        Altera o salário base do professor.
        
        :param val: Novo valor do salário.
        """
        self.__salario = val
    
    def estudar(self):
        """
        Método que define o professor estudando.
        """
        print("Professor está estudando.")
    
    def receberSalario(self, nTurmas):
       """
        Calcula o salário do professor com base no número de turmas.
        
        :param nTurmas: Número de turmas que o professor possui.
        """
       salario_atual = self.__salario * nTurmas
       print(f"Salario atual do professor: R${salario_atual}")

class ProfessorEducacaoBasica(Professor):
    """
    Classe que representa um professor de educação básica.
    """
    def elaborarProvas(self):
        """
        Cria e retorna uma prova com 5 questões.

        :return: Objeto Prova contendo 5 questões.
        """
        prova = Prova(['01', '02', '03', '04', '05'])
        return prova
    
    def corrigirProvas(self, prova):
        """
        Corrige a prova e atribui uma nota baseada no dobro da quantidade de respostas.

        :param prova: Objeto Prova a ser corrigido.
        :return: Nota atribuída à prova.
        """
        prova.nota = 2* (len(prova.respostas))
        return prova.nota

class ProfessorUniversitario(Professor):
    """
    Classe que representa um professor universitário.
    """
    def elaborarProvas(self):
        """
        Cria e retorna uma prova com 10 questões.

        :return: Objeto Prova contendo 10 questões.
        """

        prova = Prova(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10'])
        return prova

    def corrigirProvas(self, prova):
        """
        Corrige a prova e atribui uma nota baseada no número de respostas corretas.

        :param prova: Objeto Prova a ser corrigido.
        :return: Nota atribuída à prova.
        """
        prova.nota = (len(prova.respostas))
        return prova.nota
    
class Prova:
    """
    Classe que representa uma prova com questões, respostas e nota atribuída.
    """
    def __init__(self, questoes:list):
        """
        Inicializa a prova com uma lista de questões.

        :param questoes: Lista de questões da prova.
        """
        self.__questoes = questoes
        self.__respostas = []
        self.__nota = 0

    @property
    def questoes(self):
        """
        Propriedade que retorna as questões da prova.
        """
        return self.__questoes
    
    @questoes.setter
    def questoes(self, novas_questoes):
        """
        Altera as questões da prova.

        :param novas_questoes: Lista de novas questões.
        """
        self.__questoes = novas_questoes
    
    @property
    def respostas(self):
        """
        Propriedade que retorna as respostas da prova.
        """
        return self.__respostas
    
    @respostas.setter
    def respostas(self, respostas):
        """
        Altera as respostas da prova.

        :param respostas: Lista de respostas fornecidas.
        """
        self.__respostas = respostas
        
    @property
    def nota(self):
        """
        Propriedade que retorna a nota atribuída à prova.
        """
        return self.__nota
    
    @nota.setter
    def nota(self, nota_atribuida):
        """
        Altera a nota atribuída à prova.

        :param nota_atribuida: Nota a ser atribuída.
        """
        self.__nota = nota_atribuida

    
class Aluno:
    """
    Classe que representa um aluno.
    """
    def __init__(self, nome, matricula):
        """
        Inicializa o aluno com nome e matrícula.

        :param nome: Nome do aluno.
        :param matricula: Número de matrícula do aluno.
        """
        self.__nome = nome
        self.__matricula = matricula

    def fazerProva(self, prova):
        """
        Permite que o aluno faça uma prova, respondendo a questões.

        :param prova: Objeto Prova que o aluno irá responder.
        """
        print("Digite quantas questões o aluno respondeu: ")
        n = int(input())
        print("Digite as questões que o aluno respondeu(01, 02, 03...): ")
        for _ in range(n):
            resp = input()
            prova.respostas.append(resp)
        
    @property
    def nome(self):
        """
        Propriedade que retorna o nome do aluno.
        """
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        """
        Altera o nome do aluno.

        :param nome: Novo nome do aluno.
        """
        self.__nome = nome
    
    @property
    def matricula(self):
        """
        Propriedade que retorna o número de matrícula do aluno.
        """
        return self.__matricula
    
    @matricula.setter
    def matricula(self, val):
        """
        Altera o número de matrícula do aluno.

        :param val: Novo número de matrícula.
        """
        self.__matricula = val

    def estudar(self):
        """
        Método que define o aluno estudando.
        """
        print("Aluno está estudando.")

