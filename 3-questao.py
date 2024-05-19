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
    
    def inserirPrioridade(self, nodo): # Cria a função de inserção de prioridade
        # Se a lista estiver vazia ou se o primeiro nodo for verde
        if self.head is None or self.head.cor == "V": 
            # insere o novo nodo no início da lista.
            nodo.proximo = self.head 
            self.head = nodo # O novo nodo se torna o primeiro nodo
        else:
            # Procura o primeiro nodo na cor verde da lista
            nodo_atual = self.head # Começa a busca a partir do primeiro nodo
            while nodo_atual.proximo is not None and nodo_atual.proximo.cor == "A":
                # Percorre enquanto o nodo for amarelo ou a lista não acabar
                nodo_atual = nodo_atual.proximo
            # Insere o novo nodo na frente do primeiro nodo verde
            nodo.proximo = nodo_atual.proximo
            nodo_atual.proximo = nodo
    
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