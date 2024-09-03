
def ObterMedia(n1:float, n2:float, n3:float):
    return (n1+n2+n3)/3

def ObterMediaGeral(mediaAlunos:list, totalAlunos:int): 
    MediaGeral = 0
    
    for i in range(totalAlunos):
        MediaGeral += mediaAlunos[i]

    return MediaGeral/totalAlunos

mediaAlunos = []

for i in range(5):

    n1 = float(input("Digite a n1 do aluno: "))
    n2 = float(input("Digite a n2 do aluno: "))
    n3 = float(input("Digite a n3 do aluno: "))

    mediaAlunos.append(ObterMedia(n1,n2,n3))

    print(f'A média do {i+1}° aluno é {round(mediaAlunos[i],2)} ')
    
mediaTurma = ObterMediaGeral(mediaAlunos, 5)
print(f'A média da turma é {mediaTurma}')


