#       --------------practice----------------
# while loop
# Do something

# x = 1
# while  x < 10:
#     print("hello:" + str(x))
#     x = x+1

x = 1 
while x < 12:
    print("hello:" + str(x))
    x = x+1 
    z = 1
    while z<10:
        print("python:" +str(z))
        z = z+1

price = 10
while price < 50:
    print("RS:" + str(price))
    price = price + 5


n = 2
while n < 7:
    print(n)
    n = n + 2
    p = 6
    while p < 8:
        print("is less than " + str(p))
        p = p+2

#for loop 
# iterate over a sequence like range, list, strings etc
for q in range(10,100,20):
    print(f"S no: {q}" )

# for c in range(2,10):
#     if c == 6:
#         continue
#     else:
#         print(f"hello: {c}")

for c in range(2,10):
    if c == 5:
        break
    else:
        print(f"loop has ended! {c}")

countries = ["turkey", "pakistan", "india", "china", "japan"]
for c in countries:
    print(c)

string = "Family"
for p in string:
    print(p)

# ------------------Assignment-----------------------

# Display table of number 7
for table in range(1,11):
    print("7 x", table, "=", 7*table)

# Display table of number 9
for multip in range(1,15):
    print("9 x", multip, "=", multip*9)

#write a program to get factorial of 5
