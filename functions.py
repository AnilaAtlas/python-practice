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

# map() function
numList = [1,2,3,4,5,6]
def divide(x):
    return x/2
# print(map(divide,numList))
print(list(map(divide, numList)))
# now in lambda method
print(list(map(lambda y: y/y ,numList)))
print(list(map(lambda x: x+x, numList)))
print(list(map(lambda x:x-x, numList)))
print(list(map(lambda x: x*x, numList)))
print(list(map(lambda x:x%x, numList)))
print(list(map(lambda x:x**x, numList)))

# filter()
even = list(filter(lambda x: x % 2 == 0, numList))
print(even)
#  for getting odd numbers
print(list(filter(lambda x: x % 2 == 1, numList)))
# and we can get odd numbers like this
odd = list(filter(lambda p: p % 2 == 1, numList))
print(odd)

# reduce()
from functools import reduce
product = reduce(lambda total,y:total+y, numList)
print(product)