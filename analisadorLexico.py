#Tabela de cores
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
RESET = "\x1b[0m"
BOLD = "\033[1m"
NORMAL = "\033[0m"

class Token(object):

    def __init__(self, tipo, valor, linha, coluna):
        # Provavelmente vai precisar adicionar mais atributos
        self.tipo = tipo
        self.valor = valor
        self.linha = linha
        self.coluna = coluna

class Char(object):

    def __init__(self, c, lin, col):
        self.val = c # Tipo char
        self.lin = lin
        self.col = col

class Anallex:
    def __init__(self):
        # Tokens Palavras reservadas
        self.RESERVADA = "RESERVED"
        self.OPERADOR = "OPERATOR"
        self.DELIMITADOR = "SEPARATOR"
        self.IDENTIFICADOR = "IDENTIFIER"
        self.NUMERO = "INT"
        self.STRING = "STRING"
        self.TOKEN_RESERVADAS = set(["abstract", "extends", "int", "protected", "this", "boolean",
                                     "false", "new", "public", "true", "char", "import", "null",
                                     "return", "void", "class", "if", "package", "static", "while",
                                     "else", "instanceof", "private", "super"])
        # Tokens delimitadores
        self.TOKEN_DELIMITADORES = set([',', '.', '[', '{', '(', ')', '}', ']', ';'])
        # Tokens Operadores
        self.TOKEN_OPERADORES = set(['=', '==', '>', '++', '&&', '<=', '!', '-', '--', '+', '+=', '*'])
        # Lista de Tokens
        self.Tokens = []
        # Buffer da análise
        self.BuffLeitura = [] # Vai ser uma lista de Char, contendo o caractere, a linha e a coluna onde foi encontrado
        self.Linha = 0
        self.Coluna = 0
        self.openQuotes = False

    def criar_token(self, tipo, valor):
        self.Tokens.append(Token(tipo, valor, self.Linha, self.Coluna-len(valor)))

    @staticmethod
    def id_check(substr):
        # Verifica se a substring não começa com números e se os caracteres são válidos para ser identificador
        if len(substr) == 0:
            return False
        isntLetter = lambda n: (n < 65 or n > 122) or (n > 90 and n < 97) or n == 95
        isValid = lambda n: (n > 47 and n < 58) or (n > 64 and n < 91) or n == 95 or (n > 96 and n < 123) or n == 36 or n == 32
        aux = True
        if isntLetter(ord(substr[0].val)):
            i = substr[0]
            print("\"{}\" Caractere inválido para um identificador na linha {} e coluna {}".format(i.val, i.lin, i.col))
            return False
        else:
            for i in substr[1:]:
                testeChar = isValid(ord(i.val))
                aux = aux and testeChar
                if not testeChar:
                    print("\"{}\" Caractere inválido na linha {} e coluna {}".format(i.val, i.lin, i.col))
        return aux

    @staticmethod
    def num_check(substr):
        if substr == "":
            return False
        isNum = lambda n: n in range(48, 58)
        aux = True
        for i in substr:
            testeNum = isNum(ord(i.val))
            aux = aux and testeNum
        return aux

    def buff_to_str(self):
        #Converte a lista BuffLeitura pra string
        out = ""
        for c in self.BuffLeitura:
            out += c.val
        return out

    def id_or_num(self):
        if self.openQuotes:
            return
        # Aqui só é verificado se o buffer pode ser um identificador ou número
        if self.BuffLeitura == []:
            return
        elif self.num_check(self.BuffLeitura):
            self.criar_token(self.NUMERO, self.buff_to_str())
        elif self.id_check(self.BuffLeitura):
            self.criar_token(self.IDENTIFICADOR, self.buff_to_str())
        else:
            # Modo de pânico
            self.BuffLeitura = self.BuffLeitura[1:]
            self.id_or_num()
        self.BuffLeitura = []

    def lex_parser(self, novaLinha):
        self.openQuotes = False
        '''
                Essa variável 'openQuotes' é uma gambiarra pra quando o analisador encontra um começo
            de string no código. Até que ele encontre o fim dessa string, os caracteres não precisam 
            ser analisados; tudo é jogado diretamente no buffer, pra virar um token STRING
        '''
        op = ""
        ##split manual
        ##strlist = []
        for substr in novaLinha:
            # Análise rápida
            if substr in self.TOKEN_RESERVADAS:
                self.criar_token(self.RESERVADA, substr)
                self.Coluna += len(substr)+1 # +1 pelo espaço que é tirado
                continue
            # Análise caractere por caractere
            # print(substr)
            for c in substr:
                self.Coluna += 1
                # No geral, cada if serve pra identificar um tipo de token diferente
                ''' 
                        A função id_or_num é chamada toda vez que um caractere
                    especial(operador, delimitador) é encontrado para que o buffer
                    seja esvaziado e, caso haja um identificador ou número lá, que
                    o devido token seja criado
                '''
                if c == "\"" or c == "\'":
                    if not self.openQuotes:
                        self.id_or_num()
                        self.openQuotes = True
                    else:
                        self.openQuotes = False
                        self.criar_token(self.STRING, self.buff_to_str() + c)
                        self.BuffLeitura = []
                        continue
                elif self.openQuotes:
                    self.BuffLeitura.append(Char(c, self.Linha, self.Coluna))
                    continue
                if op != "" and c not in self.TOKEN_OPERADORES:
                    self.criar_token(self.OPERADOR, op)
                    op = ""
                    self.BuffLeitura.append(Char(c, self.Linha, self.Coluna))
                elif c in self.TOKEN_OPERADORES:
                    '''
                            Esse serve pra identificar operadores de um ou dois caracteres.
                        O token não é criado imediatamente após um caractere de operador
                        ser encontrado. Só após a leitura do próximo caractere que o token 
                        será criado. Por isso coloquei essa variável 'op' como um bufferzinho
                        específico pros operadores
                    '''
                    self.id_or_num()
                    if op == "":
                        if c == '+' or c == '-' or '=':
                            op += c
                        else:
                            self.criar_token(self.OPERADOR, c)
                    else:
                        if c == '+' or c == '-' or c == '=':
                            self.criar_token(self.OPERADOR, op + c)
                            op = ""
                        else:
                            self.criar_token(self.OPERADOR, c)
                elif c in self.TOKEN_DELIMITADORES:
                    self.id_or_num()
                    self.criar_token(self.DELIMITADOR, c)
                else:
                    # Se o caractere analisado não for nada especial, ele é simplesmente jogado no buffer
                    self.BuffLeitura.append(Char(c, self.Linha, self.Coluna))
                    if self.buff_to_str() in self.TOKEN_RESERVADAS:
                        self.criar_token(self.RESERVADA, self.buff_to_str())
                        self.BuffLeitura = []
            if self.openQuotes:
                self.BuffLeitura.append(Char(' ', self.Linha, self.Coluna))
            else:
                '''
                        Depois que a substring foi analisada por inteiro, pode ocorrer
                    de sobrar algo no buffer. Se não foi encontrado aspas(o que significaria
                    que nenhum caractere deve ser analisado, e sim jogado no buffer), esse algo
                    que sobrou no buffer pode ser um número ou identificador
                '''
                self.id_or_num()
            self.Coluna += 1


    def printTokens(self):
        for t in self.Tokens:
            if t.tipo == "RESERVED":
                print("< {} , {} >".format(BOLD + RED + str(t.tipo), BOLD + RED + str(t.valor) + RESET + NORMAL))
            elif t.tipo == "SEPARATOR":
                print("< {} , {} >".format(BOLD + BLUE + str(t.tipo), BOLD + BLUE + str(t.valor) + RESET + NORMAL))
            elif t.tipo == "IDENTIFIER":
                print(
                    "< {} , {} >".format(BOLD + GREEN + str(t.tipo), BOLD + GREEN + str(t.valor) + RESET + NORMAL))
            elif t.tipo == "OPERATOR":
                print("< {} , {} >".format(BOLD + CYAN + str(t.tipo), BOLD + CYAN + str(t.valor) + RESET + NORMAL))
            else:
                print(
                    "< {} , {} >".format(BOLD + MAGENTA + str(t.tipo), BOLD + MAGENTA + str(t.valor) + RESET + NORMAL))
    @staticmethod
    def contar_espacos(linha):
        if linha == "":
            return 0
        contador = 0
        for i in range(len(linha)):
            if linha[i] == ' ':
                contador += 1
            else:
                break
        return contador

    def __call__(self, arqFonte):
        # Processa arquivo com código fonte
        with open(arqFonte) as file:
            # incrementador para identificar linha atual
            for linha in file:
                self.Linha += 1
                pos = len(linha) - 1
                # Remover comentários
                if "//" in linha:
                    pos = linha.index("//")
                self.Coluna = self.contar_espacos(linha[:pos])-1
                novaLinha = linha[:pos].split()
                self.lex_parser(novaLinha)
            return self.Tokens

'''
def main():
    # Define o caminho do arquivo usado
    arquivo = 'teste1.j'
    lex = Anallex()
    return self.Tokens


if __name__ == "__main__":
    main()

# Processa o arquivo acima e inclui uma linha
'''