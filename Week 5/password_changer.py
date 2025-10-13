if __name__ == "__main__":
    while True:

        hasuppercase = 0
        haslowercase = 0
        hasdigit = 0
        hasspecial = 0
        requirements = 0

        possiblepass = input("Enter a new password: ")

        # Detecting whether the password has each type of character.

        for character in possiblepass:
            if character.isupper():
                hasuppercase = hasuppercase + 1
                requirements = requirements + 1

            elif character.islower():
                haslowercase = haslowercase + 1
                requirements = requirements + 1

            elif character.isdigit():
                hasdigit = hasdigit + 1
                requirements = requirements + 1

            else:
                hasspecial = hasspecial + 1
                requirements = requirements + 1

        if requirements < 4:
                    print("Password does not meets the requirements.")
                    print()

        if hasuppercase == 0:
                    print(" - Requires an upper case letter.")

        if haslowercase == 0:
                    print(" - Requires a lower case letter.")

        if hasdigit == 0:
                    print(" - Requires a digit/number.")

        if hasspecial == 0:
                    print(" - Requires a special character.")

        if hasuppercase and haslowercase and hasdigit and hasspecial == 1:
                    print("Password meets the requirements.")
                    print()
                    break