#data types practice

# 1: Numeric
# integer
a = 21
b = 4
var = (a + b)
print(var)

#to find the type of data
print(type(var))


#float
flo = 12
print(flo)
print (float(flo))

f = 6
print((f))
print(float(f))

dec = 77
print(dec)

  #complex (x+yj)
print(complex(dec))
print(complex(flo))
print(complex(f))
print(complex(var))


# 2: string
name = "john"
gender = "male"
print(name , gender)

# 3: sequence
#list[]
numb = [22,33,32,45]
print(numb)
print(numb[1])
print(numb[-1])

  #tuple()
tup = (2,4,6,3,1)
print(tup[2])
print(tup[2] +2)

  #range()
r = range(12)
print(list(r))

  #mapping dictionary
#(key value pair)
data ={'Devis': 2121 , 'Alexa': 2431 , 'Harry': 5656}
print(data)
print(data.keys())
print(data.values())

# 5: set
data_set = {23,56,66,77}
print(data_set)
print(set(data_set))