import time
import random
import os

# Funções
def styleprint(txt): # Função para printar estilizadamente o "txt"
    print('-'* (len(txt) + 6))
    print(f'|  {txt}  |')
    print('-'* (len(txt) + 6))

def limpar_terminal(): 
    os.system('cls' if os.name == 'nt' else 'clear')

def jogar_com_maquina(): # Função para jogar com a máquina:
    opcao = 's'
    
    while opcao == 's': # Enquanto o usuário quiser, vai rodar o código
        print('Digite sua opção: \n'
            '[1] Ímpar \n'
            '[2] Par ')
        opcao_impar_par = int(input(': '))
        while opcao_impar_par != 1 and opcao_impar_par != 2: 
            print('Você não digitou uma opção válida, tente novamente.')
            print('Digite sua opção: \n'
            '[1] Ímpar \n'
            '[2] Par ')
            opcao_impar_par = int(input(': '))

        num = int(input("Digite um número: ")) # Pede um número para o usuário 

        num_aleatorio = random.randint(0, 20)

        if opcao_impar_par == 1: 
            soma_jogo = num + num_aleatorio

            if soma_jogo % 2 == 0: 
                limpar_terminal()
                print(f'Eu escolhi {num_aleatorio}, a soma total dá: {soma_jogo} \n'
                    'Você perdeu!')
                
            else: 
                limpar_terminal()
                print(f'Eu escolhi {num_aleatorio}, a soma total dá: {soma_jogo} \n'
                    'Você ganhou!')
        
        elif opcao_impar_par == 2:
            soma_jogo = num + num_aleatorio
            if soma_jogo % 2 == 0: 
                limpar_terminal()
                print(f'Eu escolhi {num_aleatorio}, a soma total dá: {soma_jogo} \n'
                    'Você ganhou!')
            else: 
                limpar_terminal()
                print(f'Eu escolhi {num_aleatorio}, a soma total dá: {soma_jogo} \n'
                    'Você Perdeu!')     
            
        else: 
            limpar_terminal()
            print('Opção inválida.')
            continue


        # Pergunta se o usuário deseja continuar:
        opcao = input("Deseja continuar? (S/N): ").lower().strip()
        while opcao not in ('sn'): # Verifica se a opção é válida 
            print("Você não digitou uma opção válida, tente novamente: ")
            opcao = input("Deseja continuar? (S/N): ").lower().strip()

        # Se o usuário deseja sair: 
        if opcao == 'n': 
            print('Saindo', end='') # Efeito de carregamento 
            for i in range(3):
                print('.', end='', flush=True)
                time.sleep(0.3)
            
            break # Para o código
        elif opcao == 's': # Se quiser continuar, continua o código.
            time.sleep(0.3)
            limpar_terminal()
            continue

def jogar_com_player(): 

    opcao = 's'

    while opcao == 's':
        limpar_terminal()
        print('Player 1 \n'
            'Escolha sua opção: \n'
            '[1] Ímpar \n'
            '[2] Par')
        opcao_player_1 = int(input(': '))

        while opcao_player_1 != 1 and opcao_player_1 != 2: 
            print('A opção digitada não é válida.')
            print('Player 1 \n'
            'Escolha sua opção: \n'
            '[1] Ímpar \n'
            '[2] Par')
            opcao_player_1 = int(input(': '))
        
        if opcao_player_1 == 1: # Se player 1 escolheu ímpar:   
            print('Player 1')
            num_player_1 = int(input('Digite seu número: ')) # Pede o número do primeiro player
            time.sleep(0.3)
            limpar_terminal()

            print('Player 2')
            num_player_2 = int(input('Digite seu número: ')) # Pede o número do segundo player
            time.sleep(0.3)
            limpar_terminal()

            soma_jogo = num_player_1 + num_player_2

            if soma_jogo % 2 == 0: # Se for PAR
                    limpar_terminal()
                    print(f'Player 1: {num_player_1} \n'
                        f'Player 2: {num_player_2} \n'
                        f'Soma Total: {soma_jogo} \n'
                        'Jogador 2 ganhou!')
                    input('Pressione enter para continuar')
                    
            else: # Se for ÍMPAR
                limpar_terminal()
                print(f'Player 1: {num_player_1} \n'
                        f'Player 2: {num_player_2} \n'
                        f'Soma Total: {soma_jogo} \n'
                        'Jogador 1 ganhou!')
                input('Pressione enter para continuar')
                
        elif opcao_player_1 == 2: # Se player 2 escolher
            limpar_terminal() 
            print('Player 1')
            num_player_1 = int(input('Digite seu número: ')) # Pede o número do primeiro player
            time.sleep(0.3)
            limpar_terminal()

            print('Player 2')
            num_player_2 = int(input('Digite seu número: ')) # Pede o número do segundo player
            time.sleep(0.3)
            limpar_terminal()

            soma_jogo = num_player_1 + num_player_2

            if soma_jogo % 2 == 0: # Se for PAR: 
                limpar_terminal()
                print(f'Player 1: {num_player_1} \n'
                        f'Player 2: {num_player_2} \n'
                        f'Soma Total: {soma_jogo} \n'
                        'Jogador 1 ganhou!')
                input('Pressione enter para continuar')
            
            else: # Se for ÍMPAR
                limpar_terminal()
                print(f'Player 1: {num_player_1} \n'
                        f'Player 2: {num_player_2} \n'
                        f'Soma Total: {soma_jogo} \n'
                        'Jogador 2 ganhou!')
                input('Pressione enter para continuar')

        
            # Pergunta se o usuário deseja continuar:
            opcao = input("Deseja continuar? (S/N): ").lower().strip()
            while opcao not in ('sn'): # Verifica se a opção é válida 
                print("Você não digitou uma opção válida, tente novamente: ")
                opcao = input("Deseja continuar? (S/N): ").lower().strip()

            # Se o usuário deseja sair: 
            if opcao == 'n': 
                print('Saindo', end='') # Efeito de carregamento 
                for i in range(3):
                    print('.', end='', flush=True)
                    time.sleep(0.3)
                
                break # Para o código
            elif opcao == 's': # Se quiser continuar, continua o código.
                time.sleep(0.3)
                limpar_terminal()
                continue

# Código main: 
styleprint("JOGO IMPAR OU PAR")

print('Deseja jogar com a máquina ou com outro player? \n'
      '[1] Máquina \n'
      '[2] 2 Players')
opcao_maquina_ou_player = int(input(': '))

while opcao_maquina_ou_player != 1 and opcao_maquina_ou_player != 2: 
    print('Deseja jogar com a máquina ou com outro player? \n'
      '[1] Máquina \n'
      '[2] 2 Players')
    opcao_maquina_ou_player = int(input(': '))   

if opcao_maquina_ou_player == 1: 
    limpar_terminal()
    jogar_com_maquina()
elif opcao_maquina_ou_player == 2:
    limpar_terminal() 
    jogar_com_player()
else: 
    print('Opção inválida, tente novamente. ')
    