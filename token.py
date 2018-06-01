class Token:
    def __init__(self, valor, tipo, linha, coluna):
        self.valor = valor
        self.tipo = tipo
        self.linha = linha
        self.coluna = coluna

    def imprimeToken(self):
        return '[{}, ({}), {}, {}]'.format(self.tipo, self.valor, self.linha, self.coluna)