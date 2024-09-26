
import random
while True:
    play = input("do you want to play game say Y/N:")
    if play.upper() == "Y":
        print("Welcome to the game")
        lst = ["snake", "water", "gun"]
        usesr_input = input("choose one option from \n snake \n water\n gun  ")
        comp_input = random.choice(lst)
        print("computer choice", comp_input)

        if comp_input == "snake" and usesr_input == "water":
            print("Computer win and you lose")

        elif comp_input == "gun" and usesr_input == "water":
            print("Computer win and you lose")

        elif comp_input == "gun" and usesr_input == "snake":
            print("Computer win and you lose")

        elif comp_input == usesr_input:
            print("Match draw")



        else:
            print("you win")
            # gun


    else:
        print("thanks for palying game see you soon....!!!")
        break

