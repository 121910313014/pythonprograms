# ALL PROGRAMS USING FUNCTIONS IN L3
# J. Raghuramjee - 121910313004

# Function to copy elements form array
def copy_array(arr):
    # Creating another array to store elements
    arr2 = []
    # Logic to copy array elements using for loop
    for i in arr1:
        arr2.append(i) # Appending each element from arr1 to arr2
    return arr2

# Function to copy elements form array in reverse order
def copy_array_reverse(arr):
    l = len(arr)
    # Creating another array to store elements
    arr2 = []
    # Logic to copy array elements in reverse using for loop
    for i in range(l-1,-1,-1):
        arr2.append(arr[i]) # Appending each element from arr1 to arr2
    return arr2

# Function to remove duplicates
def remove_duplicates(arr):
    # Creating another array to store elements
    arr2 = []
    # Logic to remove duplicates elements from an array
    for i in arr1:
        if i not in arr2: # Checks if the element we want to add to arr2 is not in arr1
            arr2.append(i)
    return arr2

# Declaring an array to check functions
arr1 = [1,1,1,2,3,4,5,6,2,3,4,1,5,7,5,6,7,5]

print("The original array is :")
print(arr1)
print("The copied array is : ")
print(copy_array(arr1))
print("The copied array in reverse is : ")
print(copy_array_reverse(arr1))
print("The array without duplicate elements is :")
print(remove_duplicates(arr1))