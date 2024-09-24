from solucao import ProfessorUniversitario, Aluno, Prova
from random import randint

# Teste da solução
def main():
    # Criando um professor
    professor = ProfessorUniversitario("Dr. Silva", 3, 5000.0)

    # Criando um aluno
    aluno = Aluno("João", 12345)

    # Criando uma prova com questões
    questoes = ["Questão 1", "Questão 2", "Questão 3"]
    prova = Prova(questoes)

    # Simulando a elaboração e a correção da prova
    print(f"{professor.getNome()} elaborou a prova com as questões: {prova.getQuestoes()}")

    # Simulando o aluno fazendo a prova
    aluno_respostas = ["Resposta 1", "Resposta 2", "Resposta 3"]
    prova.setRespostas(aluno_respostas)
    print(f"{aluno.getNome()} respondeu: {prova.getRespostas()}")

    # Simulando a correção da prova
    nota = professor.corrigirProva(prova)
    prova.setNota(nota)
    print(f"A nota de {aluno.getNome()} na prova é: {prova.getNota()}")

if __name__ == "__main__":
    main()
