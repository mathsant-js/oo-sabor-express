import os
from modelos.Restaurante import Restaurante
from utilitarios.utilitarios import exibir_subtitulo

def exibir_nome_programa():
    """Função que exibe o nome do programa
    
    Outputs:
    - Exibe o nome do programa
    """
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)
    
def opcao_invalida():
    """Função chamada quando o usuário digita uma opção inválida
    
    Inputs:
    - Recebe uma tecla do usuário para retornar ao menu principal
    
    Ouputs:
    - Exibe mensagem Opção inválida, quando o usuário escolhe uma opção que não está presente no menu
    - Retorna função main
    
    """
    print("Opção inválida")
    input("Digite uma tecla para voltar ao menu principal: ")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

def exibir_opcoes():
    """Função que exibe as opções do programa
    
    Outputs:
    - Exibe todas as opções do programa
    """
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alterar estado do restaurante")
    print("4. Avaliar restaurante")
    print("5. Listar avaliações de um restaurante")
    print("6. Sair\n")

def escolher_opcao():
    """Função que captura escolha de opção do usuário
    
    Inputs:
    - Opção escolhida do usuário
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        match opcao_escolhida:
            case 1:
                exibir_subtitulo("Cadastrar Novo Restaurante")
                Restaurante.cadastrar_novo_restaurante()
                voltar_ao_menu_principal()
            case 2:
                exibir_subtitulo("Listando os Restaurantes")
                Restaurante.listar_restaurantes()
                voltar_ao_menu_principal()
            case 3:
                exibir_subtitulo("Alternando Estado do Restaurante")
                Restaurante.selecionar_restaurante_para_alternar_estado()
                voltar_ao_menu_principal()
            case 4:
                exibir_subtitulo("Cadastrando Avaliação de Restaurante")
                Restaurante.cadastrar_nova_avaliacao()
                voltar_ao_menu_principal()
            case 5:
                exibir_subtitulo("Listando as Avaliações de um Restaurante")
                Restaurante.listar_avaliacoes()
                voltar_ao_menu_principal()
            case 6:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
        
def voltar_ao_menu_principal():
    """Função usada para voltar ao menu principal
    
    Inputs: 
    - Recebe tecla digitada pelo usuário para retornar ao menu principal
    
    Outputs:
    - Retorna ao menu principal
    
    """
    print()
    input("Digite qualquer tecla para voltar ao menu principal: ")
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
        
def finalizar_app():
    """Função para encerrar o programa
    
    Outputs:
    - Limpa o terminal
    - Mostra mensagem de App encerrado
    
    """
    os.system("clear")
    print("App encerrado\n")