import analisadorLexico

def main():
    conteudo = ''

    # le o arquivo com o codigo fonte
    with open('./arquivosTeste/teste1.j', 'r') as arquivo:
        conteudo = arquivo.read()
    # teste se pegou o conteudo    
    #print(conteudo+'\n')

    # inicia o analisador lexico
    lexico = analisadorLexico.Lexico(conteudo)
    # cria os tokens
    tokens = lexico.criarTokens()
    # testa criacao dos tokens
    print('\nTokens: ')
    print(tokens)

# chama o main para execucao
main()    