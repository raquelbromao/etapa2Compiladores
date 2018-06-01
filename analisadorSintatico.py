# classe da árvore Binária
class AST:
    # inicializa a árvore da expressão (exp) com a raiz nula
    def __init__(self):
        self.raiz = None
 
    # função que insere valores na árvore da exp
    def inserir(self, token):
        if self.raiz == None:
            self.raiz = noElemento(token)
        #else:
            #self._insert(token, self.raiz)

# classe dos nós da árvore
class noElemento:
    # inicia um nó criando seu valor e dois filhos com valor nulo
    def __init__(self, token):
        self.token = token
        self.filhoEsquerdo = None
        self.filhoDireito = None

    def imprimeNo(self):
        return '<[{}], [({})|({})]>'.format(self.token.tipo, self.filhoEsquerdo, self.filhoDireito)   

class compilationUnit:
    def __init__(self, token, indice):
        self.token = token
        self.indice = indice

    def imprimeCompUnit(self):
        return '<[{}]->[{}]>'.format(self.token.valor, self.indice)   

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndice = 0
        #self.AST = AST()
        #self.tipos = ['DELIMITADOR', 'OPERADOR', 'RESERVADA', 'IDENTIFICADOR', 'NUMERO', 'STRING']
        
    # inicia o parser
    def parse(self):      
        primeiroToken = self.tokens[0]
        # para cada token analisa o tipo para analisar a sua determinada regra
        #if (primeiroToken.valor == 'package' or primeiroToken.valor == 'import' or ):
        while self.tokenIndice < len(self.tokens):
            tokenAtual = self.tokens[self.tokenIndice]
            print(tokenAtual.imprimeToken())

            if (tokenAtual.tipo == 'package' or tokenAtual.tipo == 'package'):
                novaCompilationUnit = compilationUnit(tokenAtual, self.tokenIndice)
                novaCompilationUnit.imprimeCompUnit()
            break    