def mergeSort(dados):
    # Verifica se a lista tem mais de 1 elemento
    if len(dados) > 1:
        # Encontra o meio da lista
        meio = len(dados)//2
        # Faz a divisão da lista em duas partes
        esquerda = dados[:meio]
        direita = dados[meio:]
        # Deixa as duas metades recursivas
        mergeSort(esquerda)
        mergeSort(direita)
        # Inicia os índices
        i = j = k = 0
        # Junta as duas metades em ordem decrescente
        while i<len(esquerda) and j<len(direita):
            # Faz a comparação dos elementos
            if esquerda[i]>direita[j]:
                # Se o lado esquerdo for maior, coloca o elemento
                # da metade esquerda na posição atual de dados
                dados[k]=esquerda[i]
                i=i+1
            else:
                # Se não for maior, coloca o elemento da
                # metade direita na posição atual de dados
                dados[k]=direita[j]
                j=j+1
            # Adiciona os dados
            k=k+1
        # Verifica se a metade esquerda ainda tem elementos
        while i < len(esquerda):
            # Adiciona os dados restantes da metade esquerda
            # nas posições de dados que restam
            dados[k]=esquerda[i]
            # Adiciona os dados
            i=i+1
            k=k+1
        # Verifica se a metade direita ainda tem elementos
        while j<len(direita):
            # Adiciona os dados restantes da metade direita
            # nas posições de dados que restam
            dados[k]=direita[j]
            # Adiciona os dados
            j=j+1
            k=k+1
# Lista de dados a serem ordenados
dados = [54, 26, 93, 17, 77, 31, 44, 55]
# Chama a função mergeSort
mergeSort(dados)
# Imprime os dados ordenados
print(dados)