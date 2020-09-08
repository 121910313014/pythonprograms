# Program to concatenate arrays
# J. Raghuramjee - 121910313004

# Taking inputs
n = int(input("Enter the number of arrays you want to concatenate : "))
arr = []
for i in range(n):
    a = []
    size = int(input("Enter the size of array " + str(i+1) + " : "))
    print("Enter the elements of array", i+1, ":")
    for i in range(size):
        ele = input()
        a.append(ele)
    arr.append(a)

# Printing the arrays
print("The arrays are : ")
for i in arr:
    print(i)

# Logic to concatenate arrays
res = []
for i in arr:
    res += i

# Printing the result
print("The concatenated array is :")
print(res)


