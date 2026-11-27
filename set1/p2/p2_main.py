# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P2 - Custom Module student_utils
# Date: November 27, 2026

import student_utils #this will import/bring the student_utils here
from student_utils import highest_grade, lowest_grade # this bring in only these functions
from datetime import datetime # I used for the report time

# user input functions starts here
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

    # print(f"{count} grade(s) saved.")
    return grades
# user input functions ends here


# output functions starts here
def display_report(grades): # this prints the result/output
    average_grade = student_utils.compute_average(grades) # this one needs the module name
    highest = highest_grade(grades) # i am able to import this function with no module name needed
    lowest = lowest_grade(grades) # this function also
    status = student_utils.status_grade(grades)
    now = datetime.now() # to get the current date and time

    print("\n=============== GRADE REPORT ====================\n")
    print(f"report generated on : {now.strftime('%B %d, %Y %I:%M %p')}")
    print(f"grades entered      : {grades}")
    print(f"average             : {average_grade:.2f}")
    print(f"highest grade       : {highest:.2f}")
    print(f"lowest grade        : {lowest:.2f}")
    print(f"status              : {status} (the passing average is {student_utils.passing_average})")
    print("\n===================================================")
# output functions ends here


# main program
def main():
    grades = enter_grades()
    display_report(grades)

main()