# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 25, 2026


# user input

def valid_grade(question):
    while True:
        try:
            grade = float(input(question))
        except ValueError:
            print("Invalid input, please type a valid grade.")
            continue
        if 0 <= grade <= 100:
            return grade
        print("grade you must input in the field are 0 and 100.")


def grade_count():
    while True:
        try:
            count = int(input("how many grades do you want to enter? "))
        except ValueError:
            print("Invalid input, please type a whole number only")
            continue
        if count >= 1:
            return count
        print("enter atleast 1 grade.")


def enter_grades():
    count = grade_count()
    grades = []
    for number in range(1, count + 1):
        grade = valid_grade(f"Enter grade {number}: ")
        grades.append(grade)

    print(f"{count} grade(s) saved.")
    return grades

def menu_options():
    print("\n======= STUDENT GRADE CALCULATOR ========")
    print("Pick a number below to perform an action")
    print("1. Enter grades")
    print("2. View results")
    print("3. Exit")


def main():
    grades = []
    while True:
        menu_options()
        choice = input("Choose an option from 1 to 3: ").strip()
        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            print("View results: ")
        elif choice == "3":
            print("exited!")
            break
        else:
            print("Invalid input, please type either 1, 2, or 3")


if __name__ == "__main__":
    main()