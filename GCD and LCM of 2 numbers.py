# Program to find GCD and LCM of two numbers
# J.Raghuramjee - 121910313004

# Creating a GCD function
def gcd(num1,num2):
	if num1==0:
		return num2
	else:
		return(gcd(num2%num1,num1))

# Taking 2 numbers as input
input1 = int(input("Enter the first number : "))
input2 = int(input("Enter the second number : "))

# Calculating the LCM and GCD of the given 2 numbers
result1 = gcd(inpu1,input2) # Caculating the 
result2 = input1*input2//result1

# Printing the answer
print("The GCD of the 2 numbers is " + str(result1) + " and the LCM of those 2 numbers is "+ str(result2))