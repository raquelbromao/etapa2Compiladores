class ErrosLexicos(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.tokenIndice = 0

    def analisaErros(self):
        while self.tokenIndice < len(self.tokens):
            tipoToken = self.tokens[self.tokenIndice][0]
            valorToken = self.tokens[self.tokenIndice][1]
            #print(tipoToken, valorToken)

            if (tipoToken == "ID_VAR" and valorToken == "var"):
                #print(tipoToken, valorToken)
                self.parserVar(self.tokens[self.tokenIndice:len(self.tokens)])
            #elif (tipoToken == "RESERVADA"):
                #print(tipoToken, valorToken)    

            self.tokenIndice += 1