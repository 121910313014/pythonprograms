# Program to print Prime numbers until a given limit
# J. Raghuramjee - 121910313004

# Taking the limit as input
n = int(input("Enter the limit : "))

print('The prime numbers till', n, 'are :')
# Logic to check prime numbers till n
for i in range(2,n+1):
    prime=True
    for j in range(2,i-1):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i,end=' ')
