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

    def qualifiedIdentifier(self, token):
        #print('Atual tokenIndice = {}'.format(self.tokenIndice))   
        if (token.tipo == 'IDENTIFICADOR'):
            return True
        else: 
            return False    

    def compilationUnit(self, token):   
        # CHECA EXISTÊNCIA DE PACKAGES
        if (token.valor == "package"): 
            print('@CompilationUnit:    < {} >'.format(token.valor))

            #  CHECA NOME DO PACOTE
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice];
            #self.qualifiedIdentifier(proximoToken)
            if (self.qualifiedIdentifier(proximoToken)):
                print('\t@QualifiedIdentifier:  < {} >'.format(proximoToken.valor))
            else: 
                print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')

            #  CHECA SE POSSUI DELIMITADOR_FIM
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice];
            if (proximoToken.valor == ';'):
                print('\t\t@Delimitador:  < ; >')
            else: 
                print('@Delimitador:\n\t\tERRO: [faltando < ; > para concluir!]')
        else: 
            print('@CompilationUnit:\n\tERRO: [sem package! Necessário criar um!]')     
        
    # inicia o parser
    def parse(self):      
        # tokenIndice = 0 
        primeiroToken = self.tokens[self.tokenIndice]

        # checa regra de compilationUnit
        if (self.compilationUnit(primeiroToken)):
            return True
        else:
            return False    
        

            

    