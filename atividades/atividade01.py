import time

# Funções
def styleprint(txt): # Função para printar estilizadamente o "txt"
    print('-'* (len(txt) + 6))
    print(f'|  {txt}  |')
    print('-'* (len(txt) + 6))

opcao = 's'

# Código: 
styleprint("CALCULO DE PAR / ÍMPAR")
while opcao == 's': # Enquanto o usuário quiser, vai rodar o código
    num = int(input("Digite um número: ")) # Pede um número para o usuário 

    if num == 0: # Se for 0: 
        print("Seu número é 0, logo, é par")
    elif num % 2 == 0: # Se o resto da divisão por 2 for igual à 0, mostra par 
        print("Seu número é par")
    else: # Se o resto da divisão por 2 for diferente de 0, mostra ímpar
        print("Ímpar")

    # Pergunta se o usuário deseja continuar:
    opcao = input("Deseja continuar? (S/N): ").lower().strip()
    while opcao not in ('sn'): # Verifica se a opção é válida 
        print("Você não digitou uma opção válida, tente novamente: ")
        opcao = input("Deseja continuar? (S/N): ").lower().strip()

    # Se o usuário deseja sair: 
    if opcao == 'n': 
        print('Saindo', end='') # Efeito de carregamento 
        for i in range(0, 3):
            print('.', end='', flush=True)
            time.sleep(0.3)
        break # Para o código
    elif opcao == 's': # Se quiser continuar, continua o código.
        continue


