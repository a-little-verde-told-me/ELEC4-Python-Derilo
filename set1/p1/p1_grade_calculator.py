# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 25, 2026


# user input

def show_menu():
    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("Pick a number below to perform an action")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []
    while True:
        show_menu()
        choice = input("Choose an option from 1 to 3: ").strip()
        if choice == "1":
            print("Enter grades: ")
        elif choice == "2":
            print("View results: ")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid input, please type either 1, 2, or 3")


if __name__ == "__main__":
    main()