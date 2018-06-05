class noElemento:
    def __init__(self, token, filhoEsquerdo, filhoDireito):
        self.token = token
        self.filhoEsquerdo = filhoEsquerdo
        self.filhoDireito = filhoDireito

class AST:
    def __init__(self, token, indice):
        self.token = token
        self.indice = indice

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndice = 0

    def classBody(self, token):
        '''
            REGRA:
        '''    
        return True

    def classDeclaration(self, token):
        '''
            REGRA:
            classDeclaration ::= class <identifier> [extends qualifiedIdentifier] classBody
        '''
        # Analisa existência da p.reservada 'class'
        if (token.valor == 'class'):
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]

            # Analisa nome da classe
            if (proximoToken.tipo == 'IDENTIFICADOR'):
                print('\t\t@Identifier:   < {} >'.format(proximoToken.valor))

                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice]

                if (proximoToken.valor == 'extends'):
                    self.tokenIndice += 1
                    proximoToken = self.tokens[self.tokenIndice]
                    if (self.qualifiedIdentifier(proximoToken)):
                        print('\t\t\t@qualifiedIdentifier:   < {} >'.format(proximoToken.valor))
                    else:
                        print('@QualifiedIdentifier:\n\t\t\tERRO: [faltando nome dos extends!]')   
                else:
                    self.classBody(proximoToken)        
            else:
                print('\t\t@Identifier: ERRO: [faltando nome da classe! necessário um!]')    
        #else:
            #print('\t@classDeclaration: ERRO: [faltando < class >!]')        

    def typeDeclaration(self, token):   
        '''
            REGRA:
            typeDeclaration ::= modifiers classDeclaration
        '''
        # VERIFICA EXISTENCIA DE CLASS
        if (token.valor == 'class'):
            print('\t@Reserved:   < {} >'.format(token.valor))
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]
            # VERIFICA EXISTENCIA DE NOME DA CLASS
            if (proximoToken.tipo == 'IDENTIFICADOR'):
                print('\t\t@Identifier:   < {} >'.format(proximoToken.valor))
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice]
                # ANALISA CLASS DECLARATION
                self.classDeclaration(proximoToken)
            else:
                print('\t\t@Identifier: ERRO: [classe sem nome! necessária criar um!]')
        else:
            print('\t@typeDeclaration: ERRO: [faltando < class >!]')    


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

            # CHECA PRÓXIMO TOKEN
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]
            # CHECA IMPORTS
            if (proximoToken.valor == 'import'):
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice];
                if (self.qualifiedIdentifier(proximoToken)):
                    print('\t@QualifiedIdentifier:  < {} >'.format(proximoToken.valor))
                else: 
                    print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')
                #qualifiedIdentifier(proximoToken)
                print('@Reserved:   < {} >'.format(proximoToken.valor));
            # typeDeclaration
            elif (proximoToken.valor in modifiers):
                print('@Modifier:   < {} >'.format(proximoToken.valor));  
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice];
                self.typeDeclaration(proximoToken)
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