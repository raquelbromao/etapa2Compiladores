import analisadorLexico
import analisadorSintatico

def main():
    #contaLinha = 0;
    conteudo = ''

    # le o arquivo com o codigo fonte
    with open('./arquivosTeste/teste1.j', 'r') as arquivo:
        conteudo = arquivo.read()
    # teste se pegou o conteudo    
    #print(conteudo+'\n')

    ''' with open('./arquivosTeste/teste1.j') as arquivo:
    for linha in arquivo:
    if "//" in linha:
    continue '''

    # inicia o analisador lexico
    print("\nIniciando análise léxica...")
    scan = analisadorLexico.Lexico(conteudo)
    # cria os tokens
    print("\tCriando os tokens...")
    tokens = scan.criarTokens()
    # testa criacao dos tokens
    print('\nTokens: ')
    #print(tokens)
    for token in tokens:
        print(token.imprimeToken())

    # inicia o analisaodor sintatico
    #print("\nIniciando a análise sintática...")
    #parse = analisadorSintatico.Parser(tokens)
    # inicia o parser
    #print("\tIniciando o parser...")
    #parse.parse()

    print("\nFim da compilação!")

# chama o main para execucao
main()    