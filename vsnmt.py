alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    alunos.sort()
    for indice, aluno in enumerate(alunos, start = 1):
        print(indice, ": " + aluno)
