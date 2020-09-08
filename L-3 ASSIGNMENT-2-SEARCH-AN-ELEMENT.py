# Program to search an element in an array
# J. Raghuramjee - 121910313004

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

ele = input("Enter the element to search : ")
search(arr,ele)