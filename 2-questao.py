import random

def embaralhaCartas(naipes, numeros):
    cartas = []
    for naipe in naipes:
        for num in numeros:
            cartas.append(f'Comprou a carta: {num} de {naipe}')
    random.shuffle(cartas)
    return cartas

def compraCartas(cartas):
    while True:
        try:
            qtd_cartas = int(input(('Insira a quantidade de cartas que deseja comprar? ')))
            if qtd_cartas > len(cartas): 
                print(f"Não há cartas suficientes disponíveis.\nRestam {len(cartas)} cartas.")
                embaralhaCartas(naipes, numeros) 
            else:
                for _ in range(qtd_cartas):
                    print(cartas.pop())
            if not cartas:  
                print("As cartas acabaram. O jogo foi finalizado.")
                return
            continuar = input('Deseja comprar mais cartas? (s/n): ')
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

naipes = ['Ouros', 'Espadas', 'Copas', 'Paus']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
cartas = embaralhaCartas(naipes, numeros)

compraCartas(cartas)