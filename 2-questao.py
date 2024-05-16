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
        qtd_cartas = int(input(('Qual a quantidade de cartas? ')))
        if qtd_cartas > len(cartas):  # Verifica se há cartas suficientes
            print(f"Não há cartas suficientes disponíveis.\nRestam {len(cartas)} cartas.")
            embaralhaCartas(naipes, numeros)  # Reembaralha as cartas
        else:
            for _ in range(qtd_cartas):
                print(cartas.pop())
        continuar = input('Deseja comprar mais cartas? (s/n): ')
        if continuar.lower() != 's':
            break

naipes = ['Ouros', 'Espadas', 'Copas', 'Paus']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
cartas = embaralhaCartas(naipes, numeros)

compraCartas(cartas)