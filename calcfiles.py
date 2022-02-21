# Keep track of users who use the calculator and what calculations they do in a file
# i.e. have a file per user

username = input("Please enter your username: ")
filename = f'{username}.txt'
# this interpolates the username stored variable with .txt to create a valid file

calcfile = open(filename, 'a+')
calcfile.write("Your calculations are:\n")

def add(num1, num2):
    ans = str(round(float(num1) + num2, 2))
    num1s = str(num1)
    num2s = str(num2)
    calc = [num1s, '+', num2s, '=', ans]
    return ans, calc

def subtract(num1, num2):
    ans = str(round(float(num1) - num2, 2))
    num1s = str(num1)
    num2s = str(num2)
    calc = [num1s, '-', num2s, '=', ans]
    return ans, calc

def multiply(num1, num2):
    ans = str(round(float(num1) * num2, 2))
    num1s = str(num1)
    num2s = str(num2)
    calc = [num1s, 'x', num2s, '=', ans]
    return ans, calc

def divide(num1, num2):
    ans = str(round(float(num1) / num2, 2))
    num1s = str(num1)
    num2s = str(num2)
    calc = [num1s, chr(247), num2s, '=', ans]
    return ans, calc

# user inputs first number and operator
num1 = float(input("Input number: "))
operator = str

# while loop if operator was not X
isFirstRun = True

while operator != 'X':
    if isFirstRun:                          # Bool for the first run-through the while loop: first input of operator
        operator = input("Input operator: ")
        isFirstRun = False                  # Set this to be False so subsequent loops use the following input for operator
    else:
        operator = input("Another operator? (You may type X to exit):").upper()

    if operator == 'X':
        print("Thank you for using this python calculator!")    # If user inputs X the program ends
        break
    elif operator != '+' and operator != '-' and operator != '*' and operator != '/':  # check if user inputs non-operator
        print("Sorry, you must input one of the following operators: +, -, *, / ")
    else:
        num2 = float(input("Input number: "))  # user inputs second number
        if num2 == 0 and operator == "/":
            print("Sorry, you cannot divide by 0.")  # divide by zero check
        else:
            if operator == "+":                          # otherwise go through valid operators using functions
                ans, calc = add(num1, num2)
            elif operator == "-":
                ans, calc = subtract(num1, num2)
            elif operator == "*":
                ans, calc = multiply(num1, num2)
            elif operator == "/":
                ans, calc = divide(num1, num2)
            else:
                print("Sorry, something has gone wrong")
            calcstring = " ".join(calc)         # make the calc list into a string using .join
            print(calcstring)                   # print this for user to see full calculation
            calc.append("\n")                   # add a new line to end of the calc list
            calcfile.writelines(calc)           # write the calculation list to file
            num1 = ans                          # reassign the num1 variable with the value from ans
else:
    print("Thank you for using this python calculator!")

# Rounding for answer means subsequent calculations lose accuracy
