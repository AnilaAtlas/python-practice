def hello():
    message = "hello viewers" #local variable
    print(message)
hello()

message2 = "Hi guys" #global variable
def greet():
    print(message2)
greet()


button = "submitted"
def btn():
    print(button)
btn()  

def is_even(num):
    return num % 2 == 0
print(is_even(9))

def addition(num1, num2):
    return num1 + num2
print(addition(5,2))

def multiply(num1, num2):
    return num1 * num2
print(multiply(3,3))

# anonymous/ lambda function:
multiply = lambda x,y: x*y
result = multiply(3,3)
print(result)

addition = lambda num1,num2: num1+num2
result = addition(5,5)
print(result)
