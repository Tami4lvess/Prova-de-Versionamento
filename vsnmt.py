# Grupo: Julia e Ágatha
alunos = []

def exibir_titulo(texto):
    print("\n" + "=" * 42)
    print(texto.center(42))
    print("=" * 42)

def organizar_alunos():
    alunos.sort(key=str.casefold)


def solicitar_nome(mensagem):
    while True:
        nome = input(mensagem).strip()

        if nome:
            return nome.title()

        print("O nome não pode ficar vazio. Tente novamente.")


def nome_ja_cadastrado(nome, indice_ignorado=None):
    for indice, aluno in enumerate(alunos):
        if indice != indice_ignorado and aluno.casefold() == nome.casefold():
            return True
    return False


def cadastrar_aluno():
    exibir_titulo("CADASTRAR ALUNO")
    nome = solicitar_nome("Digite o nome do aluno: ")

    if nome_ja_cadastrado(nome):
        print(f"O aluno {nome} já está cadastrado.")
        return

    alunos.append(nome)
    organizar_alunos()
    print(f"Aluno {nome} cadastrado com sucesso!")


def consultar_alunos():
    exibir_titulo("ALUNOS CADASTRADOS")

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return False

    organizar_alunos()
    for numero, aluno in enumerate(alunos, start=1):
        print(f"{numero:>2} - {aluno}")

    print(f"\nTotal de alunos: {len(alunos)}")
    return True


def solicitar_numero(mensagem):
    try:
        numero = int(input(mensagem))
    except ValueError:
        print("Digite um número válido.")
        return None

    if numero < 1 or numero > len(alunos):
        print("Aluno não encontrado. Escolha um número da lista.")
        return None

    return numero - 1


def atualizar_aluno():
    if not consultar_alunos():
        return

    indice = solicitar_numero("\nDigite o número do aluno que deseja atualizar: ")
    if indice is None:
        return

    nome_anterior = alunos[indice]
    novo_nome = solicitar_nome("Digite o novo nome: ")

    if nome_ja_cadastrado(novo_nome, indice):
        print(f"O aluno {novo_nome} já está cadastrado.")
        return

    alunos[indice] = novo_nome
    organizar_alunos()
    print(f"Cadastro atualizado: {nome_anterior} agora é {novo_nome}.")


def excluir_aluno():
    if not consultar_alunos():
        return

    indice = solicitar_numero("\nDigite o número do aluno que deseja excluir: ")
    if indice is None:
        return

    aluno_removido = alunos.pop(indice)
    print(f"Aluno {aluno_removido} excluído com sucesso!")


def exibir_menu():
    exibir_titulo("SISTEMA DE CADASTRO DE ALUNOS")
    print("1 - Cadastrar aluno")
    print("2 - Consultar alunos")
    print("3 - Atualizar aluno")
    print("4 - Excluir aluno")
    print("5 - Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            consultar_alunos()
        elif opcao == "3":
            atualizar_aluno()
        elif opcao == "4":
            excluir_aluno()
        elif opcao == "5":
            print("\nPrograma encerrado. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    main()
