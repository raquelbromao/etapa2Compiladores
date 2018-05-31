import re # biblioteca para uso de expressoes regulares

class Lexico(object):

    def __init__(self, codigoFonte):
        self.codigoFonte = codigoFonte

    def criarTokens(self):
        palavrasReservadas = ["float", "int", "void", "package", "import", "public", "private", "class", "static"]
        operadores = ["+", "-", "/", "%", "*", "="]

        #print('entrou no criarTokens\n')
        # variavel onde todos os tokens serao armazenados
        tokens = []

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

            # identifica palavras reservadas
            if palavra in palavrasReservadas: 
                tokens.append(["RESERVADA", palavra])

            # identifica  nomes de variaveis -> identificadores
            elif (re.match('[a-z]', palavra) or re.match('[A-Z]', palavra)):
                # se o ultimo indice do identificador tiver ';', ele e retirado e o token armazenado
                # senao tiver ';' o identificador e armazenado de uma vez
                if (palavra[len(palavra) - 1] == ";"):
                    tokens.append(["IDENTIFICADOR", palavra[0:len(palavra) -1]])
                else:    
                    tokens.append(["IDENTIFICADOR", palavra])

            # identifica numeros
            elif re.match('[0-9]', palavra):
                # se o ultimo indice do numero tiver ';', ele e retirado e o token armazenado
                # senao tiver ';' o numero e armazenado de uma vez
                if (palavra[len(palavra) - 1] == ";"):
                    tokens.append(["NUMERO", palavra[0:len(palavra) -1]])
                else:    
                    tokens.append(["NUMERO", palavra])

            # identifica operadores
            elif palavra in operadores: 
                tokens.append(["OPERADOR", palavra])

            # identifica fim de linha quando não estando junto a um outro token e quando sim
            if palavra == ";":
                tokens.append(["EXPRESSAO_FIM", ';'])
            elif (palavra[len(palavra) - 1] == ";"):
                tokens.append(["EXPRESSAO_FIM", ';'])    

            palavraIndice += 1

        # retorna os tokens criados
        return tokens    