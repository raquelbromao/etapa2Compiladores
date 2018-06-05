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

        # VERIFICA EXISTÊNCIA DE CLASS
        if (token.valor == 'class'):
            print('\t@Reserved:    < {} >'.format(token.valor))

            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]

            # VERIFICA EXISTÊNCIA DE NOME PARA A CLASSE
            if (self.analisaIdentificador(proximoToken)):
                print('\t\t@Identificador:    < {} >'.format(proximoToken.valor))

                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice]

                #Analisa Corpo da Classe
                if (proximoToken.valor == 'extends'):
                    print('\t\t\tuepa')    

            else:
                print('\t\t@Identificador: ERRO: [nome da class não é identificador! por favor, dê outro nome')  
                return False

        else:
            print('\t@Reserved: ERRO: [faltando < class >]')
            return False

        return True

    def modifiers(self, token):
        '''
            REGRA:
            modifiers ::= {public | protected | private | static | abstratc}
        '''
        modifiers = ["public", "protected", "private", "static", "abstract"]    

        if (token.valor in modifiers):
            return True
        else:
            return False        
        
    def typeDeclaration(self, token):   
        '''
            REGRA:
            typeDeclaration ::= modifiers classDeclaration
        '''

        # VERIFICA EXISTENCIA DE MODIFICADOR
        if (self.modifiers(token)):
            print('@Reserved:    < {} >'.format(token.valor))

            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]

            # ANALISA CLASSDECLARATION
            self.classDeclaration(proximoToken)

        else:
            print('@Reserved: ERRO: [faltando modificar para a classe]')
            return False

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

    def analisaIdentificador(self, token):
        if (token.tipo == 'IDENTIFICADOR'):
            return True
        else:
            return False    

    def analisaPackage(self, token):
        print('@Reserved:    < {} >'.format(token.valor))
            
        self.tokenIndice += 1
        proximoToken = self.tokens[self.tokenIndice]

        if (self.qualifiedIdentifier(proximoToken)):
            print('\t@QualifiedIdentifier:  < {} >'.format(proximoToken.valor))
        else: 
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')

        self.tokenIndice += 1
        proximoToken = self.tokens[self.tokenIndice]

        if (proximoToken.valor == ";"):
            print('\t\t@Delimitador:  < ; >')
        else:
            print('@Delimitador:\n\tERRO: [faltando < ; > para concluir!]')  

        #self.tokenIndice += 1
        #proximoToken = self.tokens[self.tokenIndice];

        return True

    def analisaImport(self, token):
        print('@Reserved:    < {} >'.format(token.valor))
            
        self.tokenIndice += 1
        proximoToken = self.tokens[self.tokenIndice]

        if (self.qualifiedIdentifier(proximoToken)):
            print('\t@QualifiedIdentifier:  < {} >'.format(proximoToken.valor))
        else: 
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')

        self.tokenIndice += 1
        proximoToken = self.tokens[self.tokenIndice]

        if (proximoToken.valor == ";"):
            print('\t\t@Delimitador:  < ; >')
        else:
            print('@Delimitador:\n\t\tERRO: [faltando < ; > para concluir!]')  

        #self.tokenIndice += 1
        #proximoToken = self.tokens[self.tokenIndice];

        return True

    def compilationUnit(self, token):   
        '''
            REGRA:
            compilationUnit ::= [package qualifiedIdentifier ;] -> 1 OU 0
                                {import qualifiedIdentifier ;}  -> 0 OU 1* 
                                {typeDeclaration} EOF           -> 0 OU 1*
        '''

        modifiers = ["public", "protected", "private", "static", "abstract"]
        print('@CompilationUnit_____________________________________________')

        # CHECA SE PRIMEIRO TOKEN É PACKAGE
        if (token.valor == "package" and self.analisaPackage(token)): 
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]

            # CHECA SE EXISTEM IMPORTS
            if (proximoToken.valor == "import" and self.analisaImport(proximoToken)):
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice]

                # CHECA SE EXISTEM CLASSES
                if (proximoToken.valor in modifiers and self.typeDeclaration(proximoToken)):
                    self.tokenIndice += 1
                    proximoToken = self.tokens[self.tokenIndice]

            # CASO NÃO HAJA IMPORTS CHECA SE EXISTE DECLARAÇÃO DE CLASSES
            elif (proximoToken.valor in modifiers and self.typeDeclaration(proximoToken)):
                print('uepa')
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice] 

        # CHECA SE PRIMEIRO TOKEN É IMPORT
        elif (token.valor == "import" and self.analisaImport(token)):
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]

            if (proximoToken.valor in modifiers and self.typeDeclaration(proximoToken)):
                print('uepa')
                self.tokenIndice += 1
                proximoToken = self.tokens[self.tokenIndice]

        # CHECA SE PRIMEIRO TOKEN É MODIFICADOR DE CLASSE   
        elif (token.valor in modifiers and self.typeDeclaration(token)):
            print('uepa')
            self.tokenIndice += 1
            proximoToken = self.tokens[self.tokenIndice]     

        return True         
        
    # inicia o parser
    def parse(self):      
        # tokenIndice = 0 
        primeiroToken = self.tokens[self.tokenIndice]

        # checa regra de compilationUnit
        if (self.compilationUnit(primeiroToken)):
            return True
        else:
            return False      