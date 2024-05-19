class ElementoDaListaSimples:
    def __init__(self, dado, cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self, nodos=None):
        self.head = None

    def inserirNoFinal(self, nodo):
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return
    
    def inserirPrioridade(self, nodo):
        nodo.proximo = self.head
        self.head = nodo
        return
    
    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == "V":
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
        return
    
filaPacientes = ListaEncadeadaSimples()

filaPacientes.inserir(1, "V")
filaPacientes.inserir(2, "V")
filaPacientes.inserir(101, "A")
filaPacientes.inserir(3, "V")
filaPacientes.inserir(102, "A")
filaPacientes.inserir(103, "A")
filaPacientes.inserir(4, "V")
filaPacientes.inserir(104, "A")
filaPacientes.inserir(105, "A")

nodo_atual = filaPacientes.head
while nodo_atual is not None:
    print(f"Cartão: {nodo_atual.cor}, Senha: {nodo_atual.dado}")
    nodo_atual = nodo_atual.proximo