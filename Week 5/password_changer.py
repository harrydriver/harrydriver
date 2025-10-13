if __name__ == "__main__":
    while True:

        possiblepass = input("Enter a new password: ")

        hasuppercase = haslowercase = hasdigit = hasspecial = False

        # Detecting whether the password has an upper case letter.

        for character in possiblepass:
            if character.isupper():
                hasuppercase = True

            elif character.islower():
                haslowercase = True

            elif character.isdigit():
                hasdigit = True

            else:
                hasspecial = True
                
            print("Password does not meet the requirements. Try Again.")

            if hasuppercase : False
            print(" - Requires an upper case letter.")

            elif haslowercase : False
            print(" - Requires a lower case letter.")

            elif hasdigit : False
            print(" - Requires a digit/number.")

            elif hasspecial : False
            print(" - Requires a special character.")

            else:
            print("Password meets the requirements.")
            print()
            continue