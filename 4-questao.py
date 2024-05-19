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
    def folhas(self, lst):
        return

Teste = BST()
Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(0)
Teste.inserir(5)
Teste.inserir(8)
Teste.inserir(13)

print('Folhas: ', Teste.folhas([]))