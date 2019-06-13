import random

import sys
def main():
    max_num = 500

    def guess():
        while True:
            gue = int(input("Guess a number"))
            if gue <= max_num and gue > 0:
                return gue
            elif gue > 500 or gue < 0:
                print("Pick a number in range 1-500")
            else:
                 print ("It has to be a number.")

    print("hello, let's play a game.")
    print("Guess a number between 1-500")
    secret_num = random.randrange(1, 501)


    while True:
        my_num = guess()
        if my_num == secret_num:
            print("congratzz!")
        elif my_num > secret_num:
            print("try smaller.")
        elif my_num < secret_num:
            print("try bigger.")
        else:
            print("type a num between 1-500")
            break

        if my_num == secret_num:
            print("YOU WON!!!")
            again = input("Wanna play again? Y/N")
            if again == str("y".lower()):
                main()

main()
