alunos = []

def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome.capitalize())
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    alunos.sort()
    for indice, aluno in enumerate(alunos, start = 1):
        print(indice, ": " + aluno)

while True:

    print("\n1 - Adicionar aluno")
    print("2 - Listar alunos")
    #print("3 - Excluir alunos")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        adicionar_aluno()



    elif opcao == "2":
        listar_alunos()

    #elif opcao == "3":
        #exclusao()
    elif opcao == "4":
        break

    else:
        print("Opção inválida!")