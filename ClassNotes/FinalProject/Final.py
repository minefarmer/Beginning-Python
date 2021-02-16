


def run():
    print("========================================")
    print("     Welcome to Super Calculator")
    print("========================================")


while True:
    print("========================================")
    print("What would you like to do?")
    print("PRESS 1 to Add:")
    print("PRESS 2 to Subtract:")
    print("PRESS 3 to Multiply:")
    print("PRESS 4 to Divide:")
    print("PRESS 5 to Find Remainder:")
    print("PRESS 6 to Use Exponents:")
    print("PRESS 7 to Quit:")
    print("========================================")

    option = int(input())

    if option == 1:
        print("--- Using Add Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(add(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 2:
        print("--- Using Subtraction Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(sub(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 3:
        print("--- Using Multplication Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(mul(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 4:
        print("--- Using Division Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(div(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 5:
        print("--- Using Modulus Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(mod(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 6:
        print("--- Using Exponent Function ---")
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(exp(a, b))

        c = int(input("Would you like to try another calculation? Press 1 for yes, 2 for NO: "))
        if c == 1:
            continue
        elif c == 2:
            break
        else:
            print("You did not choose properly.")

    elif option == 0:
        a = int(input("Input your first number: "))
        b = int(input("Input your second number: "))
        print(mod(a, b))

        c = int(input("Are you sure you want to leave? Press 1 for yes, 2 for NO: "))
        if c == 1:
            break
        elif c == 2:
            continue
        else:
            print("You did not choose properly.")
    else:
        print("Error: Yoyr input did not match the options!")

if __name__ == "__main__":
    run()
