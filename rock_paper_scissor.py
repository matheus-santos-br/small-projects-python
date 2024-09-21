import random

options = ["rock", "paper", "scissors"]

exit = False
user_points = 0
computer_points = 0

while(exit == False):
    user_input = input("Choose rock, paper, scissors or exit: ")

    computer_input = random.choice(options)

    if(user_input == "exit"):
        print("Game ended.")

        print(F"Your points {str(user_points)}")
        print(F"Computer points {str(computer_points)}")

        exit = True      

    elif(user_input == "rock"):
        print("Your input is rock")

        if(computer_input == "rock"):
            print("Computer input is rock")
            print("It's a tie!")
        elif(computer_input == "paper"):
            print("Computer input is paper")
            print("Computer wins!")
            computer_points += 1
        else:
            print("Computer input is scissors")
            print("You win!")
            user_points += 1   

    elif(user_input == "paper"):
        print("Your input is paper")

        if(computer_input == "rock"):
            print("Computer input is rock")
            print("You win!")
            user_points += 1
        elif(computer_input == "paper"):
            print("Computer input is paper")
            print("It's a tie!")
        else:
            print("Computer input is scissors")
            print("Computer wins!")
            computer_points += 1

    elif(user_input == "scissors"):
        print("Your input is scissors")
        
        if(computer_input == "rock"):
            print("Computer input is rock")
            print("Computer wins!")
            computer_points += 1
        elif(computer_input == "paper"):
            print("Computer input is paper")
            print("You win!")
            user_points += 1
        else:
            print("Computer input is scissors")
            print("It's a tie!")

    else:
        print("Invalid input")


    

    
