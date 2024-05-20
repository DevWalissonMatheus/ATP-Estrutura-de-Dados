class BST:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None
    def inserir(self, dado):
        if (self.dado == None):
            self.dado = dado
        else:
            if (dado < self.dado):
                if (self.esquerda):
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = BST(dado)
            else:
                if(self.direita):
                    self.direita.inserir(dado)
                else:
                    self.direita = BST(dado)
    def folhas(self, lst): # Cria a função folhas
        # Verifica se a árvore está vazia
        if self.dado is None:
            return lst
        # Percorre a arvore
        lstFolhas = [self]
        while lstFolhas:
            # Pega o nó do topo da pilha
            atual = lstFolhas.pop()
            # Verifica se é uma folha sem filhos
            if atual.esquerda is None and atual.direita is None:
                lst.append(atual.dado)
            # Adiciona os filhos na lista de folhas
            if atual.direita:
                lstFolhas.append(atual.direita)
            if atual.esquerda:
                lstFolhas.append(atual.esquerda)
        return lst # Retorna a lista com os valores dos nós

Teste = BST()
Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)
Teste.inserir(13)

print('Folhas: ', Teste.folhas([]))