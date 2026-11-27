# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 28, 2026

def divide_numbers(): # this will divide two numbers without crashing
    try:
        first = float(input("\nenter the first number: "))
        second = float(input("enter the second number: "))
        result = first / second
        print(f"\n{first:.2f} / {second:.2f} = {result:.2f}")
    except ValueError: # when the user entered letters instead of a number
        print("\ninvalid input, please type numbers only.")
    except ZeroDivisionError: # when the user entered 0 on the second number
        print("\nyou cannot divide by zero.")

def open_file(): # this will show the contents of a file without crashing
    file_name = input("enter the file name to open: ").strip()

    try:
        with open(file_name, "r") as file:
            contents = file.read()
        print(f"\n----- contents of {file_name} -----")
        print(contents)
        print("-----------------------------------")
    except FileNotFoundError: # when the entered file does not exist
        print(f'the file "{file_name}" was not found.')

def menu_options():
    print("\n========== SAFE MENU PROGRAM ==========")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("0. Exit")
    print("=======================================\n")


# main program
def main():
    while True:
        menu_options()
        choice = input("choose an option from 0 to 2: ").strip()
        if choice == "1":
            divide_numbers()
        elif choice == "2":
            open_file()
        elif choice == "0":
            print("\nclosing safe menu program.... byeeee!\n")
            break
        else:
            print("invalid input, please type 0, 1, or 2")

main()