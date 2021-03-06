# Program to Represent a Sparse Matrix using functions
# J. Raghuramjee - 121910313004

# Function to represent the Sparse Matrix
def sparse_matrix(arr):
    sp = []
    r = len(arr) # Number of Rows
    c = len(arr[0]) # Number of columns
    # Finding the non zero elements
    for i in range(r):
        for j in range(c):
            if arr[i][j]!=0:
                sp.append([i,j,arr[i][j]])
    return sp

# Function to print martix
def print_martix(arr):
    if arr==[]: print('EMPTY MATRIX')
    for i in arr:
        print(*i)

# Declare the 2-D matrix and printing its sparse matrix
arr = [[0,0,0,3],[0,1,3,0],[9,0,0,0],[0,0,0,4]]
print("The Original Matrix")
print_martix(arr)

print()

# Printing the sparse matrix
sparse = sparse_matrix(arr)
print("The Sparse Matrix")
print_martix(sparse)
