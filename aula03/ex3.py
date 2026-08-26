#Escreva uma função chamada cadastrar_aluno() que solicite via input o nome do aluno, sua
#idade e sua nota principal. O sistema deve armazenar esses dados em um dicionário e
#adicioná-lo a uma lista global de alunos, exibindo uma mensagem de confirmação ao final.

alunos= []

def cadastrarAluno():
    print("\n ---Cadastrar Aluno---")
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Dígite a nota principal do aluno: "))

    aluno = {
        "Nome": nome,
        "Idade": idade,
        "Nota" : nota,
    }

    alunos.append(aluno)
    print("\n---Aluno Cadastrado---")
    print("Nome", aluno["Nome"])
    print("Idade", aluno["Idade"])
    print("Nota", aluno["Nota"])
    print()
    
cadastrarAluno()