class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndice = 0

    def parse(self):
        while self.tokenIndice < len(self.tokens):
            tipoToken = self.tokens[self.tokenIndice][0]
            valorToken = self.tokens[self.tokenIndice][1]
            #print(tipoToken, valorToken)

            if (tipoToken == "ID_VAR" and valorToken == "var"):
                #print(tipoToken, valorToken)
                self.parserVar(self.tokens[self.tokenIndice:len(self.tokens)])
            #elif (tipoToken == "RESERVADA"):
                #print(tipoToken, valorToken)    

            self.tokenIndice += 1    

    def parserVar(self, streamToken):        
        #print(streamToken)
        tokensChecados = 0

        #for token in range(0, len(streamToken)):
            

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

    #def _inserir(self, valor, noAtual):

