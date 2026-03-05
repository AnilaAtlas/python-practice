student_data = {
    "name" : "David",
    "age" : 21,
    "class" : "10th",
    "section" : "A",
    "roll_no" : 1,
    "marks" : 90,
    "gender" : "male",
    "address" : "New York",
    "phone_no" : "1234567890",
    "email" : "8t2Uy@example.com",
    "father_name" : "John",
    "mother_name" : "Jane"
}

# #key function
# student_data = student_data.keys()
# print(student_data)

#value function
# student_data = student_data.values()
# print(student_data)   
# ----------------- or can use direct this function in print ---------------
# print(student_data.keys())

# copy function
# print(student_data.copy())

# get function
# print(student_data.get("class"))

# set default function
# print(student_data.setdefault("NIC", "NOT FOUND"))
# print(student_data)

# POP function --> use to remove the data keys/values 
# print(student_data.pop("name"))
# print(student_data)

# pop item function ---> use to remove the end value/key from data,so we dont need to pass an argumen in function
# print(student_data.popitem())

# clear function ---> use to clear all the data, and we dont need to pass an argument in it
# print(student_data.clear())
# print(student_data)

# items function --> use in loop and it does'nt take any argument in function
# for k,v in student_data.items():
#     print(k,v)

# for keys in student_data.items():
#     print(keys)    

# fromkeys function
# keys = ['x', 'y', 'z']
# print(student_data.fromkeys(keys, 0))

# update function -->used with dictionaries to merge another dictionary or key-value pairs into the existing one
# student_data.update({"name":"paul", "age": 22})
# print(student_data)