# Program to copy the contents from one array to another array in reverse order
# J. Raghuramjee - 121910313004

# Declaring an array to copy elements from
arr1 = [1,2,3,4,5,6,7]
l = len(arr1)
print("The array to copy elements from is : ")
print(arr1)

# Creating another array to store elements
arr2 = []

# Logic to copy array elements in reverse using for loop
for i in range(l-1,-1,-1):
    arr2.append(arr1[i]) # Appending each element from arr1 to arr2

print("The copied array in reverse is : ")
print(arr2)

# We can also copy directly by using the slicing :
# arr2  = arr1[::][::-1]
