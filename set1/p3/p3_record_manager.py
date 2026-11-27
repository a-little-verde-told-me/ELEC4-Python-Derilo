# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 27, 2026

def menu_options():
    print("\n========== STUDENT RECORD MANAGER ==========")
    print("Program by: Ian Gabriel S. Derilo")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Search a student")
    print("4. Display all students")
    print("0. Exit")


# main program
def main():
    while True:
        menu_options()
        choice = input("choose an option from 0 to 4: ").strip()
        if choice == "1":
            print("add a student: ")
        elif choice == "2":
            print("remove a student: ")
        elif choice == "3":
            print("search a student: ")
        elif choice == "4":
            print("display all students:")
        elif choice == "0":
            print("closing record manager.... byeeee!")
            break
        else:
            print("invalid input, please type 0, 1, 2, 3, or 4")
main()