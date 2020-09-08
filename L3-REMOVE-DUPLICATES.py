# Program to remove duplicates in an array
# J. Raghuramjee - 121910313004

# Declaring an array to copy elements from
arr1 = [1,1,1,2,3,4,5,6,2,3,4,1,5,7,5,6,7,5]
l = len(arr1)
print("The array to with duplicate elements is : ")
print(arr1)

# Creating another array to store elements
arr2 = []

# Logic to remove duplicates elements from an array
for i in arr1:
    if i not in arr2: # Checks if the element we want to add to arr2 is not in arr1
        arr2.append(i)

print("The array without duplicate elements is :")
print(arr2)

