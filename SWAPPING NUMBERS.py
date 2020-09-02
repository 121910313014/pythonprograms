# Program to check whether a given number is Armstrong number or not and printing the sum of its digits
# J. Raghuramjee - 121910313004

# Taking the numbers as input
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print('Before swapping, The first number is' , num1, 'and the second number is', num2)

# Swapping Logic using a temporary variable
temp = num1
num1 = num2
num2 = temp

# we can also simple swap them by a,b = b,a

print('After swapping, The first number is' , num1, 'and the second number is', num2)