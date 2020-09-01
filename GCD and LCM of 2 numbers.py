# Program to find GCD and LCM of two numbers
# J.Raghuramjee - 121910313004

# Creating a GCD function
def gcd(num1,num2):
	if num1==0:
		return num2
	else:
		return(gcd(num2%num1,num1))

# Taking 2 numbers as input
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# Computing the LCM and GCD
ans1 = gcd(a,b) # GCD of 2 numbers
ans2 = a*b//ans1 # LCM of 2 numbers

# Printing the answer
print("The GCD of 2 numbers is " + str(ans1) + " and the LCM is "+ str(ans2))