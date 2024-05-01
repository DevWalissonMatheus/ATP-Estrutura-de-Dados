def mergeSort(dados):
    if len(dados) > 1:
        meio = len(dados)//2
        esquerda = dados[:meio]
        direita = dados[meio:]
        mergeSort(esquerda)
        mergeSort(direita)
        i = j = k = 0
        while i<len(esquerda) and j<len(direita):
            if esquerda[i]<direita[j]:
                dados[k]=esquerda[i]
                i=i+1
            else:
                dados[k]=direita[j]
                j=j+1
            k=k+1
        while i<len(esquerda):
            dados[k]=esquerda[i]
            i=i+1
            k=k+1
        while j<len(direita):
            dados[k]=direita[j]
            j=j+1
            k=k+1    