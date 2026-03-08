from array import *
arr = array('i', [2,4,5,3,6,7,10,23,25,32])
print(arr)
# to find the sum of all arrays
sumOfarray = sum(arr)
print(sumOfarray)
# to find the minimun value in the array
minimumNum = min(arr)
print(minimumNum)
# to find the maximum value in the array
maxNum = max(arr)
print(maxNum)
#calcilate the average of the array elements
avrg = sum(arr) / len(arr)
print(avrg)
# reverse the array using reversed() function
array_data = [22,3,1,4,2,5,6,7]
reversd_array = list(reversed(array_data))
print(reversd_array)

# to remove duplicate elements from array using List Comprehension with set() (Preserves order)
arr = [1, 2, 2, 3, 4, 4, 5]
seen = set()
unique_arr = [x for x in arr if not (x in seen or seen.add(x))]
print(unique_arr)  # [1, 2, 3, 4, 5]
