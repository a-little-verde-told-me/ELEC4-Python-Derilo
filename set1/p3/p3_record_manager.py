# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P3 - Student Record Manager
# Date: November 27, 2026

# helper functions starts here
def format_name(name): # this function will remove extra spaces and make each word start with a capital letter
    return " ".join(name.split()).title()
# helper functions ends here

# record functions starts here
def add_student(students, added_names): # add a student to the list and prevent case-insensitive duplicates
    name = format_name(input("enter the student name to add: "))

    if name == "":
        print("the name cannot be empty.")
        return

    name_key = name.lower()
    if name_key in added_names:
        print(f"{name} is already in the list.")
        return

    students.append(name)
    added_names.add(name_key)
    print(f"{name} was added.")

def search_student(students): # find students using a whole or partial name
    keyword = input("enter a name or part of a name to search: ").strip().lower()

    if keyword == "":
        print("please type something to search.")
        return

    matches = []
    for student in sorted(students):
        if keyword in student.lower():
            matches.append(student)

    if not matches:
        print(f'no student found for "{keyword}".')
        return

    print(f"\nfound {len(matches)} student(s):")
    for number, student in enumerate(matches, start=1):
        print(f"{number}. {student}")

def remove_student(students, added_names): # remove a student from the list and the set
    if not students:
        print("the list is empty, so there is nothing to remove.")
        return

    name = format_name(input("enter the student name to remove: "))
    name_key = name.lower()

    if name_key not in added_names:
        print(f"{name} is not in the list.")
        return

    students.remove(name)
    added_names.remove(name_key)
    print(f"{name} was removed.")

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
    added_names = set()
    while True:
        menu_options()
        choice = input("choose an option from 0 to 4: ").strip()
        if choice == "1":
            add_student(students, added_names)
        elif choice == "2":
            remove_student(students, added_names)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            display_students(students)
        elif choice == "0":
            print("closing record manager.... byeeee!")
            break
        else:
            print("invalid input, please type 0, 1, 2, 3, or 4")

main()