from exercicios04 import calcular_soma_e_media

alunos = []

def obter_dados_aluno():
    nome_aluno = input('informe o seu nome completo: ')
    serie_aluno =  input('informe sua serie: ')
    email_aluno = input('informe o seu email: ')
    nota01_aluno = int(input('informe a primeira nota do aluno: '))
    nota02_aluno = int(input('informe a segunda nota do aluno: '))
    nota03_aluno = int(input('informe a terceira nota do aluno: '))
    
    return cadastrar_aluno(nome_aluno, serie_aluno, email_aluno, nota01_aluno, nota02_aluno, nota02_aluno)


def cadastrar_aluno(nome, serie, email, nota01=0, nota02=0, nota03=0):

    notas = [nota01, nota02, nota03]

    aluno = {
        'nome': nome, 
        'serie': serie, 
        'email': email,
        'notas': notas,
        'media': calcular_soma_e_media(notas)
    }

    alunos.append(nome)

    return alunos

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f'nome do aluno: {aluno['nome do aluno']} email do aluno: {aluno['email']} | serie do aluno: {aluno['serie']} | media do aluno: {aluno['media']}')
    
    return

mostrar_dados_alunos(alunos)

def iniciar_sistema():
    while True:
        print('=' *80)
        print('opcao 1 => mostrar lista de alunos cadastrados: ')
        print('opcao 2 => cadastrar alunos: ')
        print('opcao 3 => sair do sistema: ')
        print('=' *80)

        opcao = input('escolha uma das opções acima: ')

        if opcao == '1':
            mostrar_dados_alunos(alunos)
        elif opcao == '2':
            obter_dados_aluno
        else:
            print('sistema finalizado: ')

iniciar_sistema()
