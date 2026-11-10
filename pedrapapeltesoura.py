lista = ['Pedra', "Papel", "Tesoura"]

jodador1 = input("Seu nome: ")
escolha1 = input("Opções \n[1] Pedra \n[2]Papel \n[3]Tesoura \nSua escolha: ")

jogador2 = input("Seu nome: ")
escolha2 = input("Opções \n[1] Pedra \n[2]Papel \n[3]Tesoura \nSua escolha:")


# pedra papel tesoura

# escolha1 == escolha2 - empate
if escolha1 == escolha2:
    print("Empatou!")
# pedra ganha da tesoura
elif escolha1 == 1 and escolha2 == 3:
    print(f"{jogador1} ganhou!")
# tesoura ganha do papel
elif escolha1 == 3 and escolha2 == 2:
    print(f"{jogador1} ganhou!")
# papel ganha da pedra
elif escolha1 == 2 and escolha2 == 1:
    print(f"{jogador1} ganhou!")
else:
    print(f"{jogador2} ganhou!")

