# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P4 - Safe Menu Program
# Date: November 28, 2026

def menu_options():
    print("\n========== SAFE MENU PROGRAM ==========")
    print("1. Divide two numbers")
    print("2. Open a file")
    print("0. Exit")


# main program
def main():
    while True:
        menu_options()
        choice = input("choose an option from 0 to 2: ").strip()
        if choice == "1":
            print("divide two numbers: ")
        elif choice == "2":
            print("open a file: ")
        elif choice == "0":
            print("closing safe menu program.... byeeee!")
            break
        else:
            print("invalid input, please type 0, 1, or 2")

main()