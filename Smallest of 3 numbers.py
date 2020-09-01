# Program to find the smallest of 3 numbers
# J.Raghuramjee - 121910313004

# Taking the inputs 
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

# logic implementation
if (a<=b) and (a<=c): # checking if a less than both the b and c
	small = a
elif (b<=c): # checking only b since a is not less than b
	small = b
else: # assigning small to c since a and b are smaller than c
	small = c

# display the answer
print("The smallest number is " + str(small))