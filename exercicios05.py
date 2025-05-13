from exercicios04 import calcular_soma_e_media

alunos = []

def obter_dados_aluno():
    nome_aluno = input('informe o seu nome completo')
    serie_aluno =  input('informe sua serie')
    email_aluno = input('informe o seu email')
    nota01_aluno = input('informe sua nota')
    nota01_aluno = input('informe sua nota')
    nota01_aluno = input('informe sua nota')


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
    return print(dados_alunos)

mostrar_dados_alunos(alunos)
