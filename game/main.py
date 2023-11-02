import random


def run():
    options = ("piedra", "papel", "tijera")
    pc_wins = 0
    person_wins = 0
    rounds = 0
    while True:
        rounds += 1
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)
        user_option = input("piedra, papel o tijera => ").lower()
        if user_option not in options:
            print("Opcion no valida, escoge de nuevo")
            continue
        pc = random.choice(options)
        if user_option == pc:
            print("Empate!")
            print(f"Tú:{person_wins}, PC:{pc_wins}")

            continue
        elif user_option == "piedra":
            if pc == "tijera":
                person_wins += 1
                print("Ganaste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")
            else:
                pc_wins += 1
                print("Perdiste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")
        elif user_option == "papel":
            if pc == "piedra":
                person_wins += 1
                print("Ganaste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")
            else:
                pc_wins += 1
                print("Perdiste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")
        elif user_option == "tijera":
            if pc == "papel":
                person_wins += 1
                print("Ganaste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")
            else:
                pc_wins += 1
                print("Perdiste")
                print(f"Escogiste: {user_option.upper()}, PC: {pc.upper()}")
                print(f"Tú:{person_wins}, PC:{pc_wins}")

        if person_wins == 2:
            print("Eres el Ganador")
            break
        if pc_wins == 2:
            print("Gano la PC")
            break


if __name__ == "__main__":
    run()
