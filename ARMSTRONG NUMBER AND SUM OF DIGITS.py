# Program to check whether a given number is Armstrong number or not and printing the sum of its digits
# J. Raghuramjee - 121910313004

# Taking the number as input
n = int(input("Enter the number : "))

# Storing n in a duplicate values
dup_n = n
dup__n = n

# Initialsing other variables
digits = 0
sum_digits = 0
sum_digits_pow = 0

# Logic to check the sum of digits and number of digits
while dup_n!=0:
    sum_digits += dup_n%10
    digits += 1
    dup_n //= 10

# Printing the sum of digits
print("The sum of digits is", sum_digits)

# Logic to generate the sum of digits with powers
while dup__n!=0:
    sum_digits_pow += (dup__n%10)**digits
    dup__n //= 10

if sum_digits_pow==n:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")
