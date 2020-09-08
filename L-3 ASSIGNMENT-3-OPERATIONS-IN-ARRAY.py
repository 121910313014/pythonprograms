# OperationS in Array
# J. Raghuramjee - 121910313004

# Function to copy elements form array
def copy_array(arr):
    # Creating another array to store elements
    arr2 = []
    # Logic to copy array elements using for loop
    for i in arr:
        arr2.append(i) # Appending each element from arr1 to arr2
    print("Elements of the copied array are : ")
    for i in arr2:
        print(i)

# Function to remove duplicates
def remove_duplicates(arr):
    # Creating another array to store elements
    arr2 = []
    # Logic to remove duplicates elements from an array
    for i in arr:
        if i not in arr2: # Checks if the element we want to add to arr2 is not in arr1
            arr2.append(i)
    print("The array without duplicate elements is :")
    for i in arr2:
        print(i)

# Function display elements
def display(arr):
    print("The elements in the array are :")
    # Loop to go through all the elements
    for i in arr: 
        print(i)

# Function to delete element at index k
def del_at_k(arr,k):
    # Check if the index is valid
    if k>=len(arr):
        print("Enter a valid index!")
    else:
        del arr[k] # Del keyword to remove element in array
        print("The elements after deleting the array are :")
        for i in arr:
            print(i)

# Function to search an element in array
def search(arr,k):
    found = False
    # Loop to check if the element exists in array
    for index in range(len(arr)):
        if arr[index]==k:
            found = True
            print("The element", k, "is at index", index)
    # prints this statment if element doesnt exit
    if not found :print("The element does not exist")

# Taking the array as input
arr = []
n = int(input("Enter the size of the array: "))
print("Enter the elements of the array :")
for i in range(n):
    k = input()
    arr.append(k)

print("The elements of the array are : ", arr)
# Giving option to user
print("Select from the options below :")
print("Option 1 - Copy elements from this array to another array")
print("Option 2 - Remove duplicates from the array")
print("Option 3 - Delete element at k-th index")
print("Option 4 - Search for an element in the array")
print("Option 5 - Display all the elements in the array")

opt = int(input("Enter an option : "))

if opt==1:
    copy_array(arr)
elif opt==2:
    remove_duplicates(arr)
elif opt==3:
    ind = int(input("Enter the index to remove the element : "))
    del_at_k(arr,ind)
elif opt==4:
    ele = input("Enter the element to search : ")
    search(arr,ele)
elif opt==5:
    display(arr)
else:
    print("Enter a vaild input!")


