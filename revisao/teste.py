from modelo import *

class TestaSolucao:
    @staticmethod
    def main():
        # Criando professores
        prof_basica = ProfessorEducacaoBasica('João', 5, 1500)
        prof_universitario = ProfessorUniversitario('Amanda', 10, 2500)

        # Criando aluno
        aluno = Aluno('Stephany', 202400316)

        # Testando professor de educação básica
        print("Teste do Professor de Educação Básica:")
        prova_basica = prof_basica.elaborarProvas()
        print(f"Prova elaborada com {len(prova_basica.questoes)} questões")
        aluno.fazerProva(prova_basica)
        nota_basica = prof_basica.corrigirProvas(prova_basica)
        print(f"Nota da prova básica: {nota_basica}")
        prof_basica.receberSalario(prof_basica.nTurmas)
        prof_basica.estudar()

        print("\n" + "="*50 + "\n")

        # Testando professor universitário
        print("Teste do Professor Universitário:")
        prova_universitaria = prof_universitario.elaborarProvas()
        print(f"Prova elaborada com {len(prova_universitaria.questoes)} questões")
        aluno.fazerProva(prova_universitaria)
        nota_universitaria = prof_universitario.corrigirProvas(prova_universitaria)
        print(f"Nota da prova universitária: {nota_universitaria}")
        prof_universitario.receberSalario(prof_universitario.nTurmas)
        prof_universitario.estudar()

        print("\n" + "="*50 + "\n")

        # Testando aluno
        print("Teste do Aluno:")
        print(f"Nome do aluno: {aluno.nome}")
        print(f"Matrícula do aluno: {aluno.matricula}")
        aluno.estudar()

if __name__ == "__main__":
    TestaSolucao.main()