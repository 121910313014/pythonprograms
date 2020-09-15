# Program to copy the contents from one array to another array
# J. Raghuramjee - 121910313004

# Declaring an array to copy elements from
arr1 = [1,2,3,4,5,6,7]
print("The array to copy elements from is : ")
print(arr1)

# Creating another array to store elements
arr2 = []

# Logic to copy array elements using for loop
for i in arr1:
    arr2.append(i) # Appending each element from arr1 to arr2

print("The copied array is : ")
print(arr2)

# We can also copy directly by using the slicing :
# arr2  = arr1[::]
