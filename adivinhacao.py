import random;

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)  # váriavel de número que o jogador tem que acertar
    total_de_tentativas = 0  # número de vezes que o jogo irá rodar
    pontos = 1000

    print("Escolha o nível de dificuldade:")
    print("(1) Fácil")
    print("(2) Médio")
    print("(3) Difícil")

    nivel = int(input())

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    # (while) rodada = 1 #a rodada que o jogo começa

    # while(rodada <= total_de_tentativas): #conta o número de rodadas usando o (while)

    for rodada in range(1, total_de_tentativas + 1):  # conta o número de rodadas usando o (for), +1 é necessário para que o programa nao encerre em duas tentativas
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))  # String interpolation
        chute_str = input("Digite um número entre 1 e 100:")  # input para o usuário tentar adivinhar o número
        print("Você digitou ", chute_str)  # retorno para confirmar o número digitado
        chute = int(chute_str)  # transforma a string digitada pelo usuário em inteiro

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue  # "irmão do break", porém ao invés de encerrar o laço, ele irá encerrar a iteração e continuar para a próxima.

        acertou = chute == numero_secreto  # transforma a condição em uma váriavel, vale lembrar que a váriavel se torna do tipo boolean
        maior = chute > numero_secreto  # ^^
        menor = chute < numero_secreto  # ^^

        if (acertou):  # if que chama a condição inicializada anteriormente
            print("Você acertou e fez {} pontos!".format(pontos))
            break  # encerra o while caso ele acerte.
        else:  # else para tratamento de erros
            if (maior):  # outro if que chama a condição maior
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):  # if que chama a condição menor
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)#calculo de pontos, a função abs vai retornar sempre o valor absoluto, não terá negativo
            pontos = pontos - pontos_perdidos

    # (while) rodada = rodada + 1 #a cada final de tentativa ele irá aumentar uma rodada.

    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()

#versão final do jogo de adivinhação