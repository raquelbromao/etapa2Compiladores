import re # biblioteca para uso de expressoes regulares
import token

class Lexico(object):

    def __init__(self, codigoFonte):
        self.codigoFonte = codigoFonte

    def criarTokens(self):
        palavrasReservadas = ["float", "int", "void", "package", "import", "public", "private", "class", "static"]
        operadores = ["+", "-", "/", "%", "*", "="]

        #print('entrou no criarTokens\n')
        # variavel onde todos os tokens serao armazenados
        tokens = []

        #for linhas in self.codigoFonte:
            #print(linhas); 

        # cria uma lista com as  palavras contidas no codigo fonte
        listaPalavras = self.codigoFonte.split()
        # testa se separou cada expressao do codigo fonte
        #print(listaPalavras)

        # guarda o atual indice da palavra atual da listaPalavras que esta sendo lida
        palavraIndice = 0;

        # percorre listaPalavras
        while palavraIndice < len(listaPalavras):
            #print(listaPalavras[palavraIndice])
            palavra = listaPalavras[palavraIndice]

            # identifica palavra VAR
            if palavra == "var":
                novoToken = token.Token(palavra, "ID_VAR", 0, 0)
                tokens.append(novoToken)
            # identifica palavras reservadas
            elif palavra in palavrasReservadas: 
                novoToken = token.Token(palavra, "RESERVADA", 0, 0)
                tokens.append(novoToken)
            # identifica  nomes de variaveis -> identificadores
            elif (re.match('[a-z]', palavra) or re.match('[A-Z]', palavra)):
                # se o ultimo indice do identificador tiver ';', ele e retirado e o token armazenado
                # senao tiver ';' o identificador e armazenado de uma vez
                if (palavra[len(palavra) - 1] == ";"):
                    novoToken = token.Token(palavra[0:len(palavra) -1], "IDENTIFICADOR",0,0)
                    tokens.append(novoToken)
                else:
                    novoToken = token.Token(palavra, "IDENTIFICADOR", 0, 0)
                    tokens.append(novoToken)    
            # identifica numeros
            elif re.match('[0-9]', palavra):
                # se o ultimo indice do numero tiver ';', ele e retirado e o token armazenado
                # senao tiver ';' o numero e armazenado de uma vez
                if (palavra[len(palavra) - 1] == ";"):
                    novoToken = token.Token(palavra[0:len(palavra) -1], "NUMERO", 0, 0)
                    tokens.append(novoToken)
                else:    
                    novoToken = token.Token(palavra, "NUMERO", 0, 0)
                    tokens.append(novoToken)
            # identifica operadores
            elif palavra in operadores: 
                novoToken = token.Token(palavra, "OPERADOR", 0, 0)
                tokens.append(novoToken)

            # identifica fim de linha quando não estando junto a um outro token e quando sim
            if palavra == ";":
                novoToken = token.Token(";", "EXPRESSAO_FIM", 0, 0)
                tokens.append(novoToken)
            elif (palavra[len(palavra) - 1] == ";"):
                novoToken = token.Token(";", "EXPRESSAO_FIM", 0, 0)
                tokens.append(novoToken)

            palavraIndice += 1

        # retorna os tokens criados
        return tokens    