import os

restaurantes = [{'nome':'Sushi', 'categoria': 'Japonesa', 'ativo': False},
                {'nome':'Pizza Fernessa', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Japa Kombo', 'categoria': 'Japonesa', 'ativo': False}]


def exibir_nome_programa():
    print("Sabor Express \n")

def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar Restaurante")
    print("3. Alterar status do Restaurante")
    print("4. Sair \n")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla ou aperte enter para voltar ao menu principal ')
    main()

def opcao_invalida():
    print("Opção Invalida")
    voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastro de novos Restaurantes')
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulos('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo} ')

    voltar_ao_menu_principal()
def alterar_estado_restaurante():
    exibir_subtitulos('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcoes__escolhida = int(input("Escolha uma opção: "))
        if opcoes__escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcoes__escolhida == 2:
            listar_restaurantes()

        elif opcoes__escolhida == 3:
            alterar_estado_restaurante()
        elif opcoes__escolhida == 4:
            finalizarApp()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizarApp():
    exibir_subtitulos('Encerrando o App')

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()