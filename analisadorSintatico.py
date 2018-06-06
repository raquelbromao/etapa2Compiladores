import re
import estruturaAST

class Parser(object):
    def __init__(self, tokens, tokenAtual):
        self.tokens = tokens
        self.tokenIndice = 0
        self.tokenAtual = tokenAtual
        self.tokenBuff = []

    def selector(self):
        '''
            REGRA:
                selector ::= . qualifiedIdentifier [arguments] | [ expression ]
        ''' 
        if (self.tokenAtual == '.'):
            self.proximoToken()
            if (self.qualifiedIdentifier()):
                self.proximoToken()

                if (self.tokenAtual.valor == '(' and self.arguments()):
                    return True
                elif ():
                    pass
                else:
                    print('')
                    return False      
            else:
                print('')
                return False
        elif (self.tokenAtual.valor == '['):
                self.proximoToken()

                if (self.expression()):
                    self.proximoToken()

                    if (self.tokenAtual.valor == ']'):
                        return True   
                    else:
                        print('')
                        return False
                else:
                    print('')
                    return False               
        else:
            print('')
            return False

    def literal(self):
        '''
            REGRA:
                literal ::= <int_literal> | <char_literal> | <string_literal> | true | false | null
        '''    
        # Verifica se é true
        if (self.tokenAtual.valor == 'true'):
            return True
        # Verifica se é false    
        elif (self.tokenAtual.valor == 'false'):
            return True
        # Verifica se é null    
        elif (self.tokenAtual.valor == 'null'):
            return True
        # Verifica se é tipo NUMERO -> sendo então <int_literal>    
        elif (self.tokenAtual.tipo == 'NUMERO'):
            return True  
        # Verifica se é tipo identificador -> podendo ser ou <char_literal> ou <string_literal>
        # Foram usadas as seguintes regras para analisar via expressão regular:
        # <char_literal> = <"> <token que é ID e tem tamanho 1 e que só tem letra do alfabeto> <">
        # <string_literal> = <"> <> <">
        elif (self.tokenAtual.valor == ' \" '):
            self.proximoToken();

            # para <char_literal>
            if (len[self.tokenAtual.valor] == 1 and analisaIdentificador()):
                    self.proximoToken()

                    if (self.tokenAtual.valor == ' \" '):
                        return True
                    else:
                        print('')
                        return False    
            #para <string_literal>
            elif (analisaIdentificador()):
                self.proximoToken()

                if (self.tokenAtual.valor == ' \" '):
                    return True
                else:
                    print('')
                    return False 
            else:
                print('')  
                return False         
        # ERRO    
        else:
            return False    

    def variableInitializer(self):
        '''
            REGRA:
                variableInitializer ::= arrayInitializer | expression
        '''
        # Avalia se é regra arrayInitializer
        if (self.arrayInitializer()):
            return True
        # Avalia se é regra expression    
        elif (self.expression()):
            return True
        # ERRO    
        else:
            print('\n\n\n\n\n\n@variableInitializer: ERRO [esperado arrayInitializer ou expression]')
            return False

    def variableDeclarator(self):
        '''
            REGRA:
                variableDeclarator ::= <identifier> [= variableInitializer] -> 0 ou 1*
        '''    
        # Verifica se token é identificador
        if (self.analisaIdentificador()):
            self.proximoToken()

            #Verifica se há símbolo de atribuição
            if(self.tokenAtual.valor == '='):
                self.proximoToken()

                # Verifica regra variableInitializer
                if(self.variableInitializer()):
                    return True
                else:
                    print('\n\n\n\n\n\n@variableInitializer: ERRO')
                    return False 
            # se não houver símbolo de atribuição está correto tb e volta        
            else:
                return True
        else:
            print('\n\n\n\n@Identificador: ERRO [não existe identificador para a variável! por favor dê um nome]')
            return False

    def variableDeclarators(self):
        '''
            REGRA:
                variableDeclarators ::= variableDeclarator {, variableDeclarator} -> 0 ou 1* variáveis separadas por < , >
        '''    
        if (self.variableDeclarator()):
            return True
        else:
            print('\n\n\n\n@variableDeclarator: ERRO [declaração da variável]')
            return False

    def localVariableDeclarationStatement(self):
        '''
            REGRA:
                localVariableDeclarationStatement ::= type variableDeclarators ;
        '''    
        
        print('@localVariableDeclarationStatement_______________')
        #Avalia existência de declaração de tipo antes da variável
        if (self.typeAnalyser()):
            self.proximoToken()

            #Avalia a regra variableDeclarators()
            if (self.variableDeclarators()):
                self.proximoToken()

                if (self.tokenAtual.valor == ';'):
                    return True
                else:
                    print('\n\n\n@Delimitador: ERRO: [faltando < ; >]')
                    return False

            else:
                print('\n\n@variableDeclarators: ERRO: [declaração da variável]')
                return False
        else:
            print('\n@type: ERRO: [falta declaração de tipo de variável]')
            return False

    def basicType(self):
        '''
            REGRA:
                basicType ::= boolean | char | int
        '''
        tipo = ["boolean", "char", "int"]

        if (self.tokenAtual.valor in tipo):
            return True
        else:
            return False        

    def referenceType(self):
        '''
            REGRA:
                referenceType ::= basicType [ ] {[ ]} | qualifiedIdentifier {[ ]}
        '''

        # Verifica se começa com tipo básico
        if (self.basicType()):

            self.proximoToken()

            # verifica se é vetor/lista
            if (self.tokenAtual == '['):
                self.proximoToken()
                if (self.tokenAtual == ']'):
                    return True
                else:
                    return False
            else:
                return False        
        # Verifica se começa com identificador
        elif (self.qualifiedIdentifier()) :

            self.proximoToken()

            # verifica se é vetor/lista
            if (self.tokenAtual == '['):
                self.proximoToken()
                if (self.tokenAtual == ']'):
                    return True
                else:
                    return False
            elif (self.tokenAtual == ']'):
                return False
            else:
                return True    
        # Erro  
        else:
            return False

    def variableDeclarators(self):
        pass    

    def typeAnalyser(self):
        '''
            REGRA:
                type ::= referenceType | basicType
        '''
        # Verifica se o tipo é vetor ou matriz
        if (self.referenceType()):
            return True
        # Verifica se é só um tipo básico    
        elif (self.basicType()):  
            return True  
        else:
            return False

    def block(self):
        pass    

    def formalParameters(self):
        '''
            REGRA:
                formalParameters ::= ( [formalParameter {, formalParameter}] )
        '''
        pass   

    def memberDecl(self):
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

        elif self.tokenAtual.valor == "void" or self.typeAnalyser():
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

    def classBody(self):
        '''
            REGRA:  
                classBody ::= { {modifiers memberDecl} } -> 0 ou 1*
        '''    
        # checa se a classe main abriu com {
        if (self.tokenAtual.valor == '{'):
            print('@Delimitador:    < { >')

            # Analisa se a classe main foi fechada com }
            # lista[-1] -> retorna o último elemento da lista
            if (self.tokens[- 1].valor == "}"):
                print('\t@Delimitador:      < } >]')
                
                self.proximoToken()

                #Checa se possui modificador após '{'
                if (self.modifiers()):
                    # Checa se os membros foram declarados correntamente
                    self.memberDecl();
                # Caso não haja modificador class deve ser Vazio    
                # FAZER
                else:
                    pass
                    #self.proximoToken()

            else:
                print('\t@Delimitador: ERRO: [faltando < } >]')    

            return True
        else:
            print('@Delimitador: ERRO: [faltando < { >]')
            return False    

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
            if (self.analisaIdentificador()):
                print('\t\t@Identificador:    < {} >'.format(self.tokenAtual.valor))

                self.proximoToken()

                #Analisa se possui extensões
                if (self.tokenAtual.valor == 'extends'):
                    print('\t\t\t@Reserved:    < {} >'.format(self.tokenAtual.valor))

                    self.proximoToken()  

                    if (self.qualifiedIdentifier()):
                        print('\t\t\t\t@Identificador:    < {} >'.format(self.tokenAtual.valor))  

                        self.proximoToken()

                        if (self.classBody()):
                            return True  

                    else:
                        print('\t\t\t\t@classDeclaration: ERRO: [nome da extends não é identificaor! por favor, dê outro nome]')  
                        return False      

                elif (self.tokenAtual.valor == '{' and self.classBody()):
                    #print('\t\t\t #classBody#oi')
                    return True

                else:
                    print('\t\t@Identificador: ERRO: [nome da class não é identificador! por favor, dê outro nome')  
                    return False   

            else:
                print('\t\t@Identificador: ERRO: [nome da class não é identificador! por favor, dê outro nome')  
                return False

        else:
            print('\t@Reserved: ERRO: [faltando < class >]')
            return False

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
        if (self.modifiers()):
            print('@Reserved:    < {} >'.format(self.tokenAtual.valor))

            self.proximoToken()

            # ANALISA CLASSDECLARATION
            self.classDeclaration()

        else:
            print('@Reserved: ERRO: [faltando modificar para a classe]')
            return False

    def qualifiedIdentifier(self):
        '''
            REGRA:
                qualifiedIdentifier ::= <identifier> {. <identifier> }
        '''
        #print('Atual tokenIndice = {}'.format(self.tokenIndice))   
        #contador = 0

        if (self.tokenAtual.tipo == 'IDENTIFICADOR'):
            #contador += 1
            #print('[{}]'.format(contador))
            return True
        else: 
            return False    

    def analisaIdentificador(self):
        if (self.tokenAtual.tipo == 'IDENTIFICADOR'):
            return True
        else:
            return False    

    def analisaOperador(self):
        operadores = ["+", "++", "-", "--", "/", "%", "*", "=", "+=", "==", "&&", ">", "<=", "instanceof"]
        
        if (self.tokenAtual.valor in operadores):
            return True
        else:
            return False    

    def analisaPackage(self):
        print('@Reserved:    < {} >'.format(self.tokenAtual.valor))
            
        self.proximoToken()

        # checa se nome do package é identificador qualificado
        if (self.qualifiedIdentifier()):
            print('\t@QualifiedIdentifier:  < {} >'.format(self.tokenAtual.valor))

            self.proximoToken()

            # Checa se p´roximo token é ;
            if (self.tokenAtual.valor == ";"):
                print('\t\t@Delimitador:  < ; >')
                return True
            else:
                print('@Delimitador:\n\tERRO: [faltando < ; > para concluir!]')
                return False

        else: 
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')
            return False

    def analisaImport(self):
        print('@Reserved:    < {} >'.format(self.tokenAtual.valor))
        self.proximoToken()

        if (self.qualifiedIdentifier()):
            print('\t@QualifiedIdentifier:  < {} >'.format(self.tokenAtual.valor))
            self.proximoToken()

            if (self.tokenAtual.valor == ";"):
                print('\t\t@Delimitador:  < ; >')
                return True
            else:
                print('@Delimitador:\n\t\tERRO: [faltando < ; > para concluir!]')
                return False
        else: 
            print('@QualifiedIdentifier:\n\tERRO: [faltando < ; > para concluir!]')
            return False

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
        if (self.tokenAtual.valor == "package" and self.analisaPackage()): 
            self.proximoToken()

            # CHECA SE EXISTEM IMPORTS
            if (self.tokenAtual.valor == "import" and self.analisaImport()):
                self.proximoToken()

                # CHECA SE EXISTEM CLASSES
                if (self.tokenAtual.valor in modifiers and self.typeDeclaration()):
                    self.proximoToken()

            # CASO NÃO HAJA IMPORTS CHECA SE EXISTE DECLARAÇÃO DE CLASSES
            elif (self.tokenAtual.valor in modifiers and self.typeDeclaration()):
                self.proximoToken()

        # CHECA SE PRIMEIRO TOKEN É IMPORT
        elif (self.tokenAtual.valor == "import" and self.analisaImport()):
            self.proximoToken()

            if (self.tokenAtual.valor in modifiers and self.typeDeclaration()):
                self.proximoToken()

        # CHECA SE PRIMEIRO TOKEN É MODIFICADOR DE CLASSE   
        elif (self.tokenAtual.valor in modifiers and self.typeDeclaration()):
            self.proximoToken()           

        return True         
        
    def proximoToken(self):
        tamanho = len(self.tokens)

        if (self.tokenIndice > tamanho):
            print('erro')
        else:
            self.tokenIndice += 1
            self.tokenAtual = self.tokens[self.tokenIndice]

    def ultimoToken(self):
        self.tokenIndice -= 1
        self.tokenAtual = self.tokens[self.tokenIndice]  

    def salvaToken(self):
        pass    

    # inicia o parser
    def parse(self):      
        # checa regra de compilationUnit
        if (self.compilationUnit()):
            return True
        else:
            return False      