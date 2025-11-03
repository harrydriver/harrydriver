from random import randint

if __name__ == "__main__":
    try:
        sides = int(input("How many sides do you want the die to have?"))
# Checks if the user has given a value with more than one possible outcome.
        if sides < 2:
            raise ValueError("The die must have atleast 2 sides.")
# Prints message telling user they have inputted an incorrect value.
    except ValueError:
        print("You must enter a positive integer.")
# Randint is used to provide a random integer. The 1 is the number the die can roll from.
    else:
        result = randint(1, sides)
        print(f"The die rolled a: {result}")