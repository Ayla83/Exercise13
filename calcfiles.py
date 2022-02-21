# Keep track of users who use the calculator and what calculations they do in a file
# i.e. have a file per user

username = input("Please enter your username: ")
filename = f'{username}.txt'
# this interpolates the username stored variable with .txt to create a valid file

calcfile = open(filename, 'a+')
calcfile.write("Your calculations are:\n")

num1 = float(input("Input number: "))
operator = input("Input operator: ")
num2 = float(input("Input number: "))

while operator != 'X':
    if num2 == 0 and operator == "/":
        print("Sorry, you cannot divide by 0.")
    else:
        if operator == "+":
            ans = str(round(float(num1) + num2, 2))
            num1s = str(num1)
            num2s = str(num2)
            calc = [num1s, '+', num2s, '=', ans]
        elif operator == "-":
            ans = str(round(float(num1) - num2, 2))
            num1s = str(num1)
            num2s = str(num2)
            calc = [num1s, '-', num2s, '=', ans]
        elif operator == "*":
            ans = str(round(float(num1) * num2, 2))
            num1s = str(num1)
            num2s = str(num2)
            calc = [num1s, 'x', num2s, '=', ans]
        elif operator == "/":
            ans = str(round(float(num1) / num2, 2))
            num1s = str(num1)
            num2s = str(num2)
            calc = [num1s, chr(247), num2s, '=', ans]
        else:
            print("Sorry, you must input one of the following operators: +, -, *, / ")
            break
    calcstring = " ".join(calc)
    print(calcstring)
    calc.append("\n")
    calcfile.writelines(calc)
    num1 = ans
    operator = input("Another operator? (You may type X to exit):").upper()
    if operator == 'X':
        print("Thank you for using this python calculator!")
        break
    num2 = float(input("Input number: "))
else:
    print("Thank you for using this python calculator!")

# if user does not type in an operator, program crashes.
# Program needs to reach the internal if loop so that calc can be defined, or rest of program run
# Rounding for answer means subsequent calculations lose accuracy
