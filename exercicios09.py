import json
import os 

filmes = 'cadastro_filmes.jasos'


def carregar_dados():
    if os.path.exists(filmes):
        with open(filmes, 'r', encoding= 'utf-8') as arq_json: 
            return json.load(arq_json)
    else:
        return []
    
def obter_dados():
    nome_filme = input('informe o nome do filme: ')
    clasificação = input('informe o nome do filme: ')
    descrição = input('informe a descrição do filme: ')
    categoria = input('informe a categoria do filme: ')
    
    data_filme ={
        'nome_filme': nome_filme,
        'clasificação': clasificação,
        'descrição': descrição,
        'categoria': categoria,
    }

    return data_filme

def cadastrar_filme(receber_filme):
    db_filmes = carregar_dados()
    db_filmes.append(receber_filme)

    with open(filmes, 'w', encoding='utf-8') as arq_json:
        json.dump(db_filmes, arq_json indent= 4, ensure_ascii=False)

def mostrar_filmes(filmes):
    if filmes:
        for filme in filmes:
            print(f'''
                nome_filme: {filme['nome']} 
                clasificação: {filme['clasificação']}
                descrição: {filme['descrição']} 
                categoria: {filme['categoria']}
            ''')
    else:
        print('Não existe nenhum filme cadastrado.')

def iniciar_sistema():
    db_filmes = carregar_dados
    
    while True:
        print("")
        print("="*80)
        print("opcao 1 - mostrar lista de filmes ")
        print("opcao 2 - cadastrar filme")
        print("opcao 3 - sair do sistema")
        print("="*80)

        opcao = input('escolha uma das opções acima: ')

        if opcao == '1':
            mostrar_filmes()
        elif opcao == '2':
            cadastrar_filme()
        elif opcao == '3':
            print("sistema finalizado!!!")
            break
        else:
            print("Opção inválida, escolha uma das opções no menu.")

iniciar_sistema()