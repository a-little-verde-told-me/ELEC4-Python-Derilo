# Name: Ian Gabriel S. Derilo
# Section: IV-BSIT-B
# Activity: P2 - Custom Module student_utils
# Date: November 27, 2026

# global variable
passing_average = 75

# compute functions starts here
def compute_average(grades): # compute the average
    total = sum(grades)
    return total / len(grades)

def status_grade(grades): #determine the pass/fail status
    average_grade = compute_average(grades)
    if average_grade >= passing_average:
        return "passed!"
    return "failed:("
# compute functions ends here

def highest_grade(grades): # to get the highest grade
    return max(grades)  


def lowest_grade(grades): # to get the lowest grade
    return min(grades)  