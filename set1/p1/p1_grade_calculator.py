# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P1 - Student Grade Calculator
# Date: November 25, 2026

# global variable
passing_average = 75

# user input functions starts here (accept a student's grades)
def valid_grade(question): # this will validate the enteredd grade
    while True:
        try:
            grade = float(input(question))
        except ValueError:
            print("invalid input, please type a valid grade.")
            continue

        if 0 <= grade <= 100:
            return grade
        print("grade you must input in the field are 0 and 100.")


def grade_count(): # ask how many grades the user wants to input
    while True:
        try:
            count = int(input("how many grades do you want to enter? "))
        except ValueError:
            print("invalid input, type whole number only")
            continue

        if count >= 1:
            return count
        print("enter at least 1 grade.")


def enter_grades(): 
    count = grade_count()
    grades = []

    for number in range(1, count + 1):
        grade = valid_grade(f"enter grade {number}: ")
        grades.append(grade)

    print(f"{count} grade(s) saved.")
    return grades
# user input functions ends here


# compute functions starts here
def compute_average(grades): # compute the average
    total = sum(grades)
    return total / len(grades)


def highest_grade(grades): # to get the highest grade
    return max(grades)  


def lowest_grade(grades): # to get the lowest grade
    return min(grades)  


def status_grade(grades): #determine the pass/fail status
    average_grade = compute_average(grades)
    if average_grade >= passing_average:
        return "passed!"
    return "failed:("
# compute functions ends here

# output functions starts here
def display_results(grades): # this prints the result/outputs
    if not grades:
        print("\nno grades yet so choose option 1 first and input a grades.")
        return
    average_grade = compute_average(grades)
    highest = highest_grade(grades)
    lowest = lowest_grade(grades)
    status = status_grade(grades)

    print("\n=============== RESULTS ====================")
    print(f"grades entered : {grades}")
    print(f"average        : {average_grade:.2f}")
    print(f"highest grade  : {highest:.2f}")
    print(f"lowest grade   : {lowest:.2f}")
    print(f"status         : {status} (the passing average is {passing_average})")
    print("========================================")

def menu_options():
    print("\n========== STUDENT GRADE CALCULATOR ==========")
    print("Pick a number below to perform an action")
    print("1. Enter grades")
    print("2. View results")
    print("0. Exit")
# output functions ends here


# main program
def main():
    grades = []
    while True:
        menu_options()
        choice = input("choose an option from 0 to 2: ").strip()
        if choice == "1":
            grades = enter_grades()
        elif choice == "2":
            display_results(grades) 
        elif choice == "0":
            print("closing calculator, byeeee!")
            break
        else:
            print("invalid input, please type either 1, 2, or 0")
main()