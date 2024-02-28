import time
import random

caracoroa = ("cara", "coroa")
escolha = random.choice(caracoroa)
sim = ["s", "sim", "si", "im"]
while True:
    print("Bem vindo ao cara ou coroa!")
    time.sleep(2)
    print("Por favor me diga os nomes dos jogadores.")

    player = input("Jogador 1, qual o seu nome?: ")
    player2 = input("Jogador 2, qual o seu nome?: ")
    lista_players = ((player),(player2))
    escolha_player = random.choice(lista_players)

    print("Legal, vamos lá")
    print("Hm... estou decidindo qual será o jogador que vai escolher o lado primeiro")
    time.sleep(5)

    print(f"certo, já sei quem vai começar, {escolha_player} começa !")

    time.sleep(2)

    if escolha_player == player:
        player_escolha = input(f"Você escolhe, cara ou coroa?: ").lower()
        if player_escolha == "cara":
            print(f"{player} escolheu cara ! ")
            print(f"{player2} você ficou com coroa")
            time.sleep(2)
            print("Jogando a moeda...")
            time.sleep(4)
            if player_escolha == escolha:
                print(f"{player} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
            else:
                print(f"{player2} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break

        elif player_escolha == "coroa":
            print(f"{player} escolheu coroa ! ")
            print(f"{player2} você ficou com a cara")
            time.sleep(2)
            print("Jogando a moeda...")
            time.sleep(4)
            if player_escolha == escolha:
                print(f"{player} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
            else:
                print(f"{player2} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
        else:
            print("VOCÊ SÓ PODE ESCOLHER APENAS ENTRE CARA OU COROA")

    else:
        player2_escolha = input(f"Você escolhe, cara ou coroa?: ").lower()
        if player2_escolha == "cara":
            print(f"{player2} escolheu cara ! ")
            print(f"{player} você ficou com coroa")
            time.sleep(2)
            print("Jogando a moeda...")
            time.sleep(4)
            if player2_escolha == escolha:
                print(f"{player} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
            else:
                print(f"{player2} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
        elif player2_escolha == "coroa":
            print(f"{player2} escolheu coroa ! ")
            print(f"{player} você ficou com cara")
            time.sleep(2)
            print("Jogando a moeda...")
            time.sleep(4)
            if player2_escolha == escolha:
                print(f"{player2} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
            else:
                print(f"{player} ganhou ! ")
                jogar_novamente = input("Deseja jogar novamente?: ")
                if jogar_novamente in sim:
                    pass
                else:
                    break
        else:
            print("VOCÊ SÓ PODE ESCOLHER APENAS ENTRE CARA OU COROA")
            pass


