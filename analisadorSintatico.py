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
    def __init__(self, tokens, tokenAtual):
        self.tokens = tokens
        self.tokenIndice = 0
        self.tokenAtual = tokenAtual

    def classBody(self, token):
        '''
            REGRA:
        '''
        return True

    def classDeclaration(self):
        '''
            REGRA:
            classDeclaration ::= class <identifier> [extends qualifiedIdentifier] classBody
        '''

        # VERIFICA EXISTÊNCIA DE CLASS
        if (self.tokenAtual.valor == 'class'):
            print('\t@Reserved:    < {} >'.format(self.tokenAtual.valor))

            self.proximoToken()

            # VERIFICA EXISTÊNCIA DE NOME PARA A CLASSE
            if (self.analisaIdentificador(self.tokenAtual)):
                print('\t\t@Identificador:    < {} >'.format(self.tokenAtual.valor))

                self.proximoToken()

                # Analisa se possui extensões
                if (self.tokenAtual.valor == 'extends'):
                    print('\t\t\t@Reserved:    < {} >'.format(self.tokenAtual.valor))

                    self.proximoToken()

                    if (self.qualifiedIdentifier(self.tokenAtual)):
                        print('\t\t\t\t@Identificador:    < {} >'.format(self.tokenAtual.valor))

            else:
                print('\t\t@Identificador: ERRO: [nome da class não é identificador! por favor, dê outro nome')
                return False

        else:
            print('\t@Reserved: ERRO: [faltando < class >]')
            return False

        return True

    def modifiers(self):
        '''
            REGRA:
            modifiers ::= {public | protected | private | static | abstratc}
        '''
        modifiers = ["public", "protected", "private", "static", "abstract"]

        if (self.tokenAtual.valor in modifiers):
            return True
        else:
            return False

    def typeDeclaration(self):
        '''
            REGRA:
            typeDeclaration ::= modifiers classDeclaration
        '''

        # VERIFICA EXISTENCIA DE MODIFICADOR
        if (self.modifiers(self.tokenAtual)):
            print('@Reserved:    < {} >'.format(self.tokenAtual.valor))

            self.proximoToken()

            # ANALISA CLASSDECLARATION
            self.classDeclaration(self.tokenAtual)

        else:
            print('@Reserved: ERRO: [faltando modificar para a classe]')
            return False

    def qualifiedIdentifier(self):
        '''
            REGRA:
            qualifiedIdentifier ::= <identifier> {. <identifier> }
        '''
        # print('Atual tokenIndice = {}'.format(self.tokenIndice))
        # contador = 0

        if (self.tokenAtual.tipo == 'IDENTIFICADOR'):
            # contador += 1
            # print('[{}]'.format(contador))
            return True
        else:
            return False

    def analisaIdentificador(self):
        if (self.tokenAtual.tipo == 'IDENTIFICADOR'):
            return True
        else:
            return False

    def analisaPackage(self):
        print('@Reserved:    < {} >'.format(self.tokenAtual.valor))

        self.proximoToken()

        if (self.qualifiedIdentifier(self.tokenAtual)):
            print('\t@QualifiedIdentifier:  < {} >'.format(self.tokenAtual.valor))
        else:
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')

        self.proximoToken()

        if (self.tokenAtual.valor == ";"):
            print('\t\t@Delimitador:  < ; >')
        else:
            print('@Delimitador:\n\tERRO: [faltando < ; > para concluir!]')

            # self.tokenIndice += 1
        # proximoToken = self.tokens[self.tokenIndice];

        return True

    def analisaImport(self):
        print('@Reserved:    < {} >'.format(self.tokenAtual.valor))

        self.proximoToken()

        if (self.qualifiedIdentifier(self.tokenAtual)):
            print('\t@QualifiedIdentifier:  < {} >'.format(self.tokenAtual.valor))
        else:
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')

        self.proximoToken()

        if (self.tokenAtual.valor == ";"):
            print('\t\t@Delimitador:  < ; >')
        else:
            print('@Delimitador:\n\t\tERRO: [faltando < ; > para concluir!]')

            # self.tokenIndice += 1
        # proximoToken = self.tokens[self.tokenIndice];

        return True

    def compilationUnit(self):
        '''
            REGRA:
            compilationUnit ::= [package qualifiedIdentifier ;] -> 1 OU 0
                                {import qualifiedIdentifier ;}  -> 0 OU 1*
                                {typeDeclaration} EOF           -> 0 OU 1*
        '''

        modifiers = ["public", "protected", "private", "static", "abstract"]
        print('@CompilationUnit_____________________________________________')

        # CHECA SE PRIMEIRO TOKEN É PACKAGE
        if (self.tokenAtual.valor == "package" and self.analisaPackage(self.tokenAtual)):
            self.proximoToken()

            # CHECA SE EXISTEM IMPORTS
            if (self.tokenAtual.valor == "import" and self.analisaImport(self.tokenAtual)):
                self.proximoToken()

                # CHECA SE EXISTEM CLASSES
                if (self.tokenAtual.valor in modifiers and self.typeDeclaration(self.tokenAtual)):
                    self.proximoToken()

            # CASO NÃO HAJA IMPORTS CHECA SE EXISTE DECLARAÇÃO DE CLASSES
            elif (self.tokenAtual.valor in modifiers and self.typeDeclaration(self.tokenAtual)):
                self.proximoToken()

        # CHECA SE PRIMEIRO TOKEN É IMPORT
        elif (self.tokenAtual.valor == "import" and self.analisaImport(self.tokenAtual)):
            self.proximoToken()

            if (self.tokenAtual.valor in modifiers and self.typeDeclaration(self.tokenAtual)):
                self.proximoToken()

        # CHECA SE PRIMEIRO TOKEN É MODIFICADOR DE CLASSE
        elif (self.tokenAtual.valor in modifiers and self.typeDeclaration(self.tokenAtual)):
            self.proximoToken()

        return True

    def memberDeclaration(self):
        '''

        REGRA:
         memberDecl ::= <identifier> // constructor
                        formalParameters block
                        | (void | type) <identifier> // method
                        formalParameters (block | ;)
                        | type variableDeclarators ; // field
        '''
        if self.analisaIdentificador():
            self.proximoToken()
            if(self.formalParameters()):
                if self.block():
                    return True
        elif self.tokenAtual.valor == "void" or self.type():
            self.proximoToken()
            if self.analisaIdentificador():
                if self.formalParameters():
                    if self.block() or self.tokenAtual.valor == ";":
                        return True
            elif self.type():
                if self.variableDeclarators():
                    return True
        else:
            return False


    def formalParameters(self):
        '''
        REGRA:
        formalParameters ::= ( [formalParameter {, formalParameter}] )

        '''
        if self.tokenAtual.valor == "(":
            self.proximoToken()
            while self.formalParameter():
                self.proximoToken()
                if self.tokenAtual.valor != ",":
                    return False
                self.proximoToken()
            if self.tokenAtual == ")":
                return True

    def type(self):
        '''
        REGRA:
        type ::= referenceType | basicType

        '''
        return self.referenceType() or self.basicType()

    def basicType(self):
        '''
        REGRA:
        basicType ::= boolean | char | int
        '''
        aux = self.tokenAtual.valor
        if aux == "boolean" or aux == "char" or aux == "int":
            return True
        else:
            return False

    def referenceType(self):
        '''
        REGRA:
        referenceType ::= basicType [ ] {[ ]}
                        | qualifiedIdentifier {[ ]}
        '''
        return self.basicType() or self.qualifiedIdentifier()

    def block(self):
        '''
        REGRA:
        block ::= { {blockStatement} }
        '''
        if self.tokenAtual.valor == "{":
            self.proximoToken()
            while self.blockStatement():
                pass
        #terminando ainda


    def proximoToken(self):
        self.tokenIndice += 1
        self.tokenAtual = self.tokens[self.tokenIndice]

    # inicia o parser
    def parse(self):
        # checa regra de compilationUnit
        if (self.compilationUnit()):
            return True
        else:
            return False      