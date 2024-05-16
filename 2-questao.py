import random

def embaralhaCartas(naipes, numeros):
    cartas = []
    for naipe in naipes:
        for num in numeros:
            cartas.append(f'{num} de {naipe}')
    random.shuffle(cartas)
    return cartas

def compraCartas(cartas):
    qtd_cartas = int(input('Qual a quantidade de cartas?\n'))
    for _ in range(qtd_cartas):
        print(cartas.pop())

naipes = ['Ouros', 'Espadas', 'Copas', 'Paus']
numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
cartas = embaralhaCartas(naipes, numeros)

compraCartas(cartas)