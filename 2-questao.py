import random # Importa uma biblioteca para embaralhar as cartas de forma aleatória
# Cria uma função para embaralhar as cartas que 
# recebe as variáveis naipes e  números
def embaralhaCartas(naipes, numeros):
    cartas = [] # Lista vazia para guardar as cartas
    for naipe in naipes: # Cria um loop para os naipes 
        for num in numeros: # Cria um loop para os números
            # Adiciona a combinação dos naipes e números na lista cartas
            cartas.append(f'Comprou a carta: {num} de {naipe}')
    random.shuffle(cartas) # Embaralha as cartas
    return cartas # Retorna as cartas embaralhadas
# Cria a função para comprar as cartas que recebe a variável cartas
def compraCartas(cartas):
    while True: # Loop para perguntar se o usuário quer comprar mais cartas
        try: # Inicia um try para evitar erros
            if modo == '1': # Se for escolhido o modo 1
                # Pergunta a quantidade de cartas que deseja comprar
                qtd_cartas = int(input('Quantas cartas deseja comprar? '))
            else: # Se for escolhido o modo 2
                # Compra 3 cartas por rodada
                qtd_cartas = 3
            if qtd_cartas > len(cartas): # Verifica se ha cartas suficientes na pilha
                # Se não houverem mais cartas informa que a quantidade é menor 
                # que a quantidade solicitada e informa a quantidade restante
                print(f"Não há cartas suficientes disponíveis.\nRestam apenas {len(cartas)} cartas.")
            else: # Se a quantidade for suficiente compra as cartas
                for _ in range(qtd_cartas): # Loop para retirar a quantidade desejada
                    print(cartas.pop()) # Remove e imprime a carta da pilha
            if not cartas: 
                # Se as cartas acabarem informa o usuário e encerra o jogo
                print("As cartas acabaram.\nO jogo foi finalizado.")
                return
            # Se ainda restarem cartas pergunta ao usuário se quer continuar comprando
            continuar = input('Deseja comprar mais cartas? (s/n): ')
            if continuar.lower() != 's': # Se a resposta for diferente de "s"
                # Encerra o jogo
                break
        except ValueError: # Captura exceções de valor inválido
            # Informa ao usuário que deve inserir um valor numérico
            print("Por favor, insira um número inteiro válido.")

naipes = ['Ouros', 'Espadas', 'Copas', 'Paus'] # Define os naipes das cartas
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] # Define os números das cartas
cartas = embaralhaCartas(naipes, numeros) # Embaralha as cartas e armazena na lista cartas
# Pergunta ao usuário qual modo de jogo deseja
modo = input('Escolha o modo de jogo:'
            '\nDigite "1" para escolher a quantidade de cartas' 
            '\nDigite "2" para comprar 3 cartas por rodada'
            '\n>> ').strip() # .strip remove espaços em branco do início e do fim da string
while modo not in ['1', '2']: # Se for inserido algo diferente de 1 ou 2
    # Informa que é um modo inválido e refaz a pergunta
    modo = input('Modo inválido. Escolha "1" ou "2": ').strip()

compraCartas(cartas) # Chama a função para começar o modo de jogo escolhido