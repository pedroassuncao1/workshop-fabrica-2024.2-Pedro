class Carro: # Criando a classe carro
    def __init__(self, marca="", modelo="", batido=False, pneus_novos=False, ano=0): # Criando o construtor da classe
        self.marca = marca
        self.modelo = modelo 
        self.batido = batido
        self.pneu_novos = pneus_novos
        self.ano = ano
    
    # Função para coletar os dados do carro
    def coletar_dados(self):
        self.marca = input("Digite a marca do carro: ")
        self.modelo = input("Digite o modelo do carro: ")
        self.batido = input("O carro é batido? (True/False): ").strip().lower() == 'true'
        self.pneu_novos = input("Os pneus são novos? (True/False): ").strip().lower() == 'true'
        self.ano = int(input("Digite o ano do carro: "))

    def conselho(self): # Criando o método conselho
        pontos_positivos = 0 

        if not self.batido: 
            pontos_positivos += 1
        if self.pneu_novos: 
            pontos_positivos += 1

        # Verificar o ano do veículo: 
        if 2019 <= self.ano < 2021: 
            pontos_positivos += 1
        elif 2021 <= self.ano < 2024: 
            pontos_positivos += 2
        elif self.ano == 2024: 
            pontos_positivos += 3

        # Verificar quantos pontos foram obtidos:
        if pontos_positivos == 0: 
            conselho = "Não é recomendado comprar o carro."
        elif pontos_positivos == 1: 
            conselho = "O carro vai dar trabalho para dar lucro."
        elif 2 <= pontos_positivos <= 4:
            conselho = "O carro é um bom investimento."
        else: 
            conselho = "O carro é um ótimo investimento."
        
        return conselho
    

# Criando o objeto carro: 
carro = Carro() # Instanciar a classe

# Coletar os dados do carro
carro.coletar_dados()

# Imprimir o conselho:
print(carro.conselho())
