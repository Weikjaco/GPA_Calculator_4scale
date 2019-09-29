# -----------------------------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Jacob Weikert
# Last Modified: September 15, 2017 
# -----------------------------------------------------------------------
#   
# **LAB ASSIGNMENT**:
#   
# 1. This program asks for:
#   1.1 The amount of classes taken.
#   1.2 The letter grades recieved for each class.
#   1.3 The number of credits that each class were worth.
#
# 2. This program then calculates and informs the user their overall GPA.
# -----------------------------------------------------------------------
# **HONOR'S LAB ENHANCEMENT**:
#
#       1. Can calculate total GPA for a students whole college career.
#
#       2. The user can enter any value into any of the prompts, and will
#          be able to try again.
#
#       3. Calculates how many credits worth of A's are needed to raise
#          their total GPA to any desired GPA value.
#
#          For exmaple, if the user wanted to see how many credits of A's were
#          needed to raise their 2.5 GPA to a 3.6 GPA, they could do this.
#
#       Exceptions:
#
#           A. If the user inputs a GPA that is lower then their
#           current GPA, they will then be informed to try again.
#
#           B. Raising a total GPA to a 4.0 is impossible after getting
#           anything lower then an "A" in school. A 4.0 will not be a valid
#           input,and the user will be informed to try again.
#
# -----------------------------------------------------------------------
import math

def newline ():
    print()

def calculate_totalcredits ():
    global totcredits
    for i in range(len(c_value)):
        totcredits = c_value[i] + totcredits

#User Input Function, that ensures no value errors are present.
def userInp (flag, prompt, apology):
    while True:
        try:
            if (flag == 1):
                value = int(input(prompt))
            else:
                value = round(float(input(prompt)),2)
        except ValueError:
            newline()
            print(apology)
            continue
        else:
            break

    return value
#-----------------------------------------------------------------------------        
def translate (grade):
    if grade.upper().strip() == 'A+' or grade.upper().strip() == 'A':
        g_value.append(4.0)
    elif grade.upper().strip() == 'A-':
        g_value.append(3.7)
    elif grade.upper().strip() == 'B+':
        g_value.append(3.3)
    elif grade.upper().strip() == 'B':
        g_value.append(3.0)
    elif grade.upper().strip() == 'B-':
        g_value.append(2.7)
    elif grade.upper().strip() == 'C+':
        g_value.append(2.3)
    elif grade.upper().strip() == 'C':
        g_value.append(2.0)
    elif grade.upper().strip() == 'C-':
        g_value.append(1.7)
    elif grade.upper().strip() == 'D+':
        g_value.append(1.3)
    elif grade.upper().strip() == 'D':
        g_value.append(1.0)
    elif grade.upper().strip() == 'F':
        g_value.append(0.0)
    else:
        newline()
        print('Please enter a valid academic letter grade.')
        grade = str(input('Enter grade for course 1 ' + str(course) + ':'))
        translate(grade)

## Define Global Variables.
        
g_value = []
c_value = []
totcredits = 0 
totgpa = 0

## Prompts user for number of courses.
coursetot = userInp(1, 'Enter the number of courses you are taking: ', '''Sorry, please enter a valid number. Type as '2' not 'two'.''')         
newline()

## Collects information for each course.

for course in range (1, coursetot + 1):
    grade = str(input('Enter grade for course ' + str(course) + ': '))
    translate(grade)
    credit = userInp(1, 'Enter credits for course ' + str(course) + ': ', '''Sorry, please enter a valid number. Type as '1' not 'one'.''')        
    newline()
    c_value.append(credit)
    
## Calculates total credits for GPA calculation.
    
calculate_totalcredits()

## Calculates total GPA.

for i in range (0, len(g_value)):
    totgpa = (g_value[i] * c_value[i])/(totcredits) + totgpa

## Displays total GPA to user.
    
print("Your GPA is " + str(round((totgpa),2)))

## Desired GPA. **EXTRA CODE FOR HONORS**

newline()
desired_gpa = userInp(0, 'What is your desired GPA? Enter values between 0.00-3.99: ', '''Sorry, please enter a valid number between 0.00 and 3.99. ''')

def desiredgpa ():
    global desired_gpa
    global totgpa
    global totcredits
    if desired_gpa > totgpa and desired_gpa <= 3.99:
        credits_needed = ((desired_gpa*totcredits) - (totgpa * totcredits))/(4-desired_gpa)
        return math.ceil(credits_needed)
    else:
        print('Please chose a number between your CURRENT GPA and up to 3.99.')
        newline()
        if (totgpa < 4):
            desired_gpa = userInp(0, 'What is your desired GPA? Enter values between 0.00-3.99: ', '''Sorry, please enter a valid number between 0.00 and 3.99. ''')
        

newline()
print('You need ' + str(desiredgpa()) + ''' credits worth of A's to reach your desired GPA.''')
