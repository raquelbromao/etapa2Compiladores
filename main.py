import analisadorLexico
import analisadorSintatico

def main():
    conteudo = ''

    # le o arquivo com o codigo fonte
    with open('./arquivosTeste/teste1.j', 'r') as arquivo:
        conteudo = arquivo.read()
    # teste se pegou o conteudo    
    #print(conteudo+'\n')

    # inicia o analisador lexico
    print("\nIniciando análise léxica...")
    lexico = analisadorLexico.Lexico(conteudo)
    # cria os tokens
    print("\tCriando os tokens...")
    tokens = lexico.criarTokens()
    # testa criacao dos tokens
    #print('\nTokens: ')
    #print(tokens)

    # inicia o analisaodor sintatico
    print("\nIniciando a análise sintática...")
    parser = analisadorSintatico.Parser(tokens)

    print("Fim do compilador!")

# chama o main para execucao
main()    