# Program to check whether a given number is perfect or not
# J. Raghuramjee - 121910313004

# Taking the number as input
n = int(input("Enter the number : "))
dup_n = n # Storing n in a duplicate value

# Initialsing the sum of factors to zero
factor_sum = 0  

# Logic to check whether a number is perfect
for i in range(1,n-1):
    if dup_n%i==0:
        factor_sum += i

# Checking if the number is perfect
if factor_sum==n:
    print('Yes,', n, 'is a perfect number')
else:
    print('No,', n, 'is not a perfect number')