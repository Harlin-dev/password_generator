import string
import random

def generate_password(length, char_list):
    password = []
    for i in range(length):
        randomchar = random.choice(char_list)
        password.append(randomchar)
    return "*******" + "".join(password) + "*******"

def get_character_choices():
    return ("Choose from the following:\n" 
      "1. Uppercase\n"
      "2. Lowercase\n"
      "3. Numbers\n"
      "4. Special Characters\n"
      "5. Generate\n")

def main():
    char_list = ""

    print("Welcome to Harlin's password generator!")

    length = int(input("How many characters would you like? "))

    print(get_character_choices())

    while True:
        choice = input('Enter your parameters: ')
        if choice == "1":
            char_list += string.ascii_uppercase
        elif choice == "2":
            char_list += string.ascii_lowercase
        elif choice == "3":
            char_list += string.digits
        elif choice == "4":
            char_list += string.punctuation

        elif choice == "5":
            if len(char_list) == 0:
                print("Please pick a valid option")
            else:
                break

        else:
            print("Please pick a valid option")

    result = generate_password(length, char_list)
    print(result)

    while True:
        choice = input("Would you like to: \n"
                       "1. Regenerate\n"
                       "2. Change Parameters\n"
                       "3. Exit\n"
                       )
        if choice == "1":

            print(generate_password(length, char_list))


        elif choice == "2":
            char_list = ''
            length = int(input("How many characters "))
            print(get_character_choices())

            while True:
                choice = input('Enter your parameters: ')
                if choice == "1":
                    char_list += string.ascii_uppercase
                elif choice == "2":
                    char_list += string.ascii_lowercase
                elif choice == "3":
                    char_list += string.digits
                elif choice == "4":
                    char_list += string.punctuation

                elif choice == "5":
                    if len(char_list) == 0:
                        print("Please pick a valid option")
                    else:
                        break

                else:
                    print("Please pick a valid option")

            print(generate_password(length, char_list))

        elif choice == "3":
            break

if __name__ == "__main__":
    main()















