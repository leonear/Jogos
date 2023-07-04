import random;
def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto (TRUE)
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            print("Voce errou! Ainda faltam {} tentativas".format(6-erros))
            erros += 1
            desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do Jogo")




def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")




def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()                       #remove o \n ao final da linha
        palavras.append(linha)                      #adiciona as linhas para a lista palavras

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()      #o comando upper transorma todas as letras em maiuscalas, ignorando o tipo delas

    return palavra_secreta




def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]           #lista para armazenar cada letra acertada da string da palavra secreta
                                                    #for letra in palavra_secreta: -forma tradicional, porém no python é possivel fazer isso direto dentro da lista
                                                        #letras_acertadas.append("_")




def pede_chute():
    chute = input("Qual letra?")
    chute = chute.strip().upper()                # o comando strip ignora os espaços em branco eventuais

    return chute




def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1




def imprime_mensagem_vencedor():
    print("Você ganhou!")



def imprime_mensagem_perdedor():
    print("Você perdeu!")



def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    ______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       __________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()






#função .count() procura o número de ocorrencias de um valor específico
#função .index() verifica o indice do valor passado

#tupla ou em inglês tuple, é uma lista imutável, ou seja não é possivel usar as funções append ou pop
#para criar uma tupla ao invés de uma lista convencional bastar utilizar '()' ao invés de '[]'
#é possível transformar listas em tuplas utilizando o comando tuple(), e o contrário com o comando list()
#é possivel colocar tuples dentro de listas e vice versa

#set é um outro tipo de lista a qual não é possivel repetir valores, para isso é utilizado as chaves'{}'
#no set para adicionar um elemento se utiliza add, ao invés de append
#set não tem indice, logo ele não segue uma ordem
#sendo assim set é uma coleção não ordenada de elementos, onde não existem elimentos duplicados

#vale lembrar que uma string também é considerado um sequência como a lista, porém de caracteres

#para leitura de arquivos utilizamos a string r, para escrever utilizamos string w e para adicionar utilizamos a string a