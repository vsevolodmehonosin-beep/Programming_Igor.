import random
import time
pun = 0

def choise():
    try:
        n = int(input("1 - rock, 2 - scissors, 3 - paper   | "))
    except:

        print("Write only numbers!")
        return None, None
    if n < 1 or n > 3:
        print("Please, sellect 1, 2 or 3!")
        return None, None
    a = random.randint(1, 3)
    return n, a

def print_rock():
    print(" ▄███▄")
    print("███████")
    print(" ▀███▀")

def print_scissors():
    print("█▄   ▄█")
    print(" ▀█▄█▀")
    print(" ▄█▀█▄")
    print("█▀   ▀█")

def print_paper():
    print("╔══════╗")
    print("║░░░░░░║")
    print("║░░░░░░║")
    print("╚══════╝")

while True:
        n, a = choise()
        if n is None:
            continue
        
        print_functions = [print_rock, print_scissors, print_paper]
        print("Your choice:")
        print_functions[n - 1]()
        time.sleep(0.5)
        print("Computer's choice:")
        print_functions[a - 1]()


        if n == 3 and a == 1:
            pun = pun + 1
            time.sleep(0.2)
            print("You win!, you have " + str(pun) + " points!")
        elif n == 2 and a == 3:
            pun = pun + 1
            time.sleep(0.2)
            print("You win!, you have " + str(pun) + " points!")
        elif n == 1 and a == 2:
            pun = pun + 1
            time.sleep(0.2)
            print("You win!, you have " + str(pun) + " points!")
        elif n == a:
            time.sleep(0.2)
            print("Let's play again!")
        else:
            time.sleep(0.2)
            print("You lose!")