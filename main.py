import analisadorLexico
import analisadorSintatico

def main():
    #contaLinha = 0;
    conteudo = ''

    # le o arquivo com o codigo fonte
    '''with open('./arquivosTeste/teste1.j', 'r') as arquivo:
        conteudo = arquivo.read()
    # teste se pegou o conteudo    
    #print(conteudo+'\n')'''

    ''' with open('./arquivosTeste/teste1.j') as arquivo:
    for linha in arquivo:
    if "//" in linha:
    continue '''

    arquivo = './arquivosTeste/listaTokens.j'

    # inicia o analisador lexico
    print("\nIniciando análise léxica...")
    scan = analisadorLexico.Anallex()
    # cria os tokens
    print("\tCriando os tokens...")
    tokens = scan(arquivo)
    # testa criacao dos tokens
    print('\nTokens: ')
    '''for token in tokens:
        print('{}|{}'.format(token.tipo, token.valor))'''

    # inicia o analisaodor sintatico
    print("\nIniciando a análise sintática...")
    parse = analisadorSintatico.Parser(tokens, tokens[0])
    # inicia o parser
    print("\tIniciando o parser...\n")
    parse.parse()

    print("\nFim da compilação!")

# chama o main para execucao
main()    