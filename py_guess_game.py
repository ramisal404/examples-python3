import random

import sys
def main():
    max_num = 500
    greet_text = "hello, let's play a game."
    guess_text = "Guess a number between 1-500"
    pick_a_num_text = "Pick a number in range 1-500"
    congrats_text = "congratzz!"
    you_won_text = "YOU WON!!!"
    bigger_text = "try bigger."
    smaller_text = "try smaller."

    def guess():
        while True:
            gue = int(input("Guess a number"))
            if gue <= max_num and gue > 0:
                return gue
            elif gue > 500 or gue < 0:
                print(pick_a_num_text)
            else:
                 print ("It has to be a number.")

    print(greet_text)
    print(guess_text)
    secret_num = random.randrange(1, 501)


    while True:
        my_num = guess()
        if my_num == secret_num:
            print(congrats_text)
        elif my_num > secret_num:
            print(smaller_text)
        elif my_num < secret_num:
            print(bigger_text)
        else:
            print("type a num between 1-500")
            break

        if my_num == secret_num:
            print(you_won_text)
            again = input("Wanna play again? Y/N")
            if again == str("y".lower()):
                main()

main()
