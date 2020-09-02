# Program to print Twin Primes until a given limit
# J. Raghuramjee - 121910313004

# Taking the limit as input
n = int(input("Enter the limit : "))

# Creating a list to store all prime numbers till n
l = []

# Logic to check prime numbers till n
for i in range(2,n+1):
	prime = True
	for j in range(2,i-1):
		if i%j == 0:
			prime = False
			break
	if prime: l.append(i)

print('The twin primes till ' + str(n) + ' are :')
# Loop to check if the adjacent primes differ by 2 and if yes, print them
for i in range(len(l)-1):
	if l[i+1]-l[i]==2:
		print('(' + str(l[i]) + ',' + str(l[i+1]) + ')', end = ' ')