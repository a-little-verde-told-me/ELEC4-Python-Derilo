# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 27, 2026

# helper functions starts here
def format_name(name): # this function will remove extra spaces and make each word start with a capital letter
    return " ".join(name.split()).title()
# helper functions ends here

# record functions starts here
def add_student(students): # add a student to the list
    name = format_name(input("enter the student name to add: "))

    if name == "":
        print("the name cannot be empty.")
        return

    students.append(name)
    print(f"{name} was added.")


def display_students(students): # show all students in alphabetical order
    if not students:
        print("\nno students yet.")
        return

    print("\n=============== STUDENT LIST ================")
    for number, student in enumerate(sorted(students), start=1):
        print(f"{number}. {student}")
    print(f"total students: {len(students)}")
    print("=============================================")
# record functions ends here

def menu_options():
    print("\n========== STUDENT RECORD MANAGER ==========")
    print("1. Add a student")
    print("2. Remove a student")
    print("3. Search a student")
    print("4. Display all students")
    print("0. Exit")


# main program
def main():
    students = []
    while True:
        menu_options()
        choice = input("choose an option from 0 to 4: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            print("remove a student: ")
        elif choice == "3":
            print("search a student: ")
        elif choice == "4":
            display_students(students)
        elif choice == "0":
            print("closing record manager.... byeeee!")
            break
        else:
            print("invalid input, please type 0, 1, 2, 3, or 4")
main()