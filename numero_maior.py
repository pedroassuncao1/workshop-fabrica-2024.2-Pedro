# Verificar qual o maior número entre três números. 

def verificar(x, y, z):

    # Variáveis para salvar o maior
    maior = None
    maior_real = None
    

    # Qual o maior número entre x e y: 
    if x > y: # Se x for maior que y
        maior = x # Maior recebe x
    
    else: # Se y maior que x
        maior = y # Maior recebe y

    
    # Verificando se o maior entre (x e y) é maior ou menor que z: 
    # Se maior for maior que z
    if maior > z: 
        maior_real = maior # maior_real recebe o valor da variável maior
    else: # Se z for maior que (maior)
        maior_real = z # (maior_real) recebe maior

    # Retorna o maior numero entre (x, y e z)
    return maior_real

# Pede os três valores
x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))

# Mostra qual o maior
print(f'O maior número é: {verificar(x, y, z)}')
    
    

