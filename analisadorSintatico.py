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
        '''
            REGRA:
            qualifiedIdentifier ::= <identifier> {. <identifier> }
        '''
        #print('Atual tokenIndice = {}'.format(self.tokenIndice))   
        if (token.tipo == 'IDENTIFICADOR'):
            return True
        else: 
            return False    

    def compilationUnit(self, token):   
        '''
            REGRA:
            compilationUnit ::= [package qualifiedIdentifier ;]
                                {import qualifiedIdentifier ;}
                                {typeDeclaration} EOF
        '''
        modifiers = ["public", "protected", "private", "static", "abstract"]

        print('@CompilationUnit_____________________________________________')
        # CHECA EXISTÊNCIA DE PACKAGES
        if (token.valor == "package"): 
            print('@Reserved:    < {} >'.format(token.valor))

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

            # CHECA SE POSSUI IMPORTS
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]
            # CHECA IMPORTS
            if (proximoToken.valor == 'import'):
                # funcao checa imports
                #qualifiedIdentifier(proximoToken)
                print('@Reserved:   < {} >'.format(proximoToken.valor));
            # CHECA DECLARAÇÃO DE CLASSES    
            elif (proximoToken.valor in modifiers):
                #typeDeclaration(proximoToken)
                print('@Modifier:   < {} >'.format(proximoToken.valor));  
            # CHECA ERROS    
            else:
                print('@Other:   < {} >'.format(proximoToken.valor));          

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
        

            

    