import random

def roll_dice():
    
    roll = input("Roll the dice? (Yes/No): ")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print(F"dice rolled: {dice1} and {dice2}")

        roll = input("Roll again? (Yes/No): ")

roll_dice()