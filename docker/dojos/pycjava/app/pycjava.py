def batalhar(escolha1, escolha2):
    if escolha1 == escolha2:
        return 'nenhum'
    if escolha1 == 'c':
        if escolha2 == 'java':
            return escolha2
        return escolha1
    if escolha1 == 'py':
        if escolha2 == 'c':
            return escolha2
        return escolha1
    if escolha1 == 'java':
        if escolha2 == 'py':
            return 'py'
        return 'java'
    return "ERROR"


def verifica_escolha(escolha):
    if escolha != 'c' and escolha != 'java' and escolha != 'py':
        return (False)
    else:
        return (True)


def get_escolha(player):
    escolha = input("Player %d : Faça sua escolha, c, py ou java : " % player)
    if (verifica_escolha(escolha) == False):
        print("Opção inválida")
        return (get_escolha(player))
    else:
        return (escolha)


if (__name__ == "__main__"):
    print("Bem vindo ao Py-C-Java")
    escolha1 = get_escolha(1)
    escolha2 = get_escolha(2)
    ganhador = batalhar(escolha1, escolha2)
    if (ganhador == "nenhum"):
        print("Empate ")
    elif(escolha1 == ganhador):
        print("Player 1 ganhou, %s ganha de %s" % (escolha1, escolha2))
    else:
        print("Player 2 ganhou, %s ganha de %s" % (escolha2, escolha1))
