class Parser(object):
    def __init__(self, tokens):
        

# classe dos nós da árvore
class noElemento:
    # inicia um nó criando seu valor e dois filhos com valor nulo
    def __init__(self, valor = None):
        self.valor = valor
        self.filhoEsquerdo = None
        self.filhoDireito = None

# classe da árvore Binária
class arvoreBinaria:
    # inicializa a árvore da expressão (exp) com a raiz nula
    def __init__(self):
        self.raiz = None
 
    # função que insere valores na árvore da exp
    def inserir(self, valor):
        if self.raiz == None:
            self.raiz = noElemento(valor)
        else:
            self._insert(valor, self.raiz)    

    def _inserir(self, valor, noAtual):

