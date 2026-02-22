# Calculator using conditions in python:
num1 = float(input("Please Enter your first number:"))
num2 = float(input("Please Enter your second number:"))
operators = input("Please Enter an Operator to perform:")

if operators == "+":
    print("The sum of the numbers is:", num1 + num2)
elif operators == "-":
    print("The Subtraction of numbers is:", num1 - num2)
elif operators == "*":
    print("The multiplication of numbers is:", num1 * num2)
elif operators == "/":
    print("The division of numbers is:", num1 / num2)
elif operators == "%":
    print("The modulus of the numbers is:", num1 % num2)
else:
    print("The entered operation is incorrect!")