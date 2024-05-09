import random

papel = 1
pedra = 2
tesoura = 3

def pedraPapelTesoura(jogador1, jogador2):
    if jogador1 == jogador2:
        return 0
    elif jogador1 == papel and jogador2 == pedra:
        return 1
    elif jogador1 == papel and jogador2 == tesoura:
        return 2
    elif jogador1 == pedra and jogador2 == papel:
        return 2
    elif jogador1 == pedra and jogador2 == tesoura:
        return 1
    elif jogador1 == tesoura and jogador2 == papel:
        return 1
    elif jogador1 == tesoura and jogador2 == pedra:
        return 2

def main():
    print("Jogo de Pedra, Papel e Tesoura")
    if(int(input("Contra CPU - Escolha 1\nContra outro jogador - Escolha 2\n")) == 1):
        jogador1 = int(input("Jogador 1: "))
        cpu = random.randint(1, 3)
        print("CPU: ", cpu)
        resultado = pedraPapelTesoura(jogador1, cpu)
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print("Jogador 1 ganhou")
        else:
            print("CPU ganhou")
    else:
        jogador1 = int(input("Jogador 1: "))
        jogador2 = int(input("Jogador 2: "))
        resultado = pedraPapelTesoura(jogador1, jogador2)
        if resultado == 0:
            print("Empate")
        elif resultado == 1:
            print("Jogador 1 ganhou")
        else:
            print("Jogador 2 ganhou")

main()