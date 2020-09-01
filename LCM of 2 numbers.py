# Program to find the LCM of 2 numbers
# J. Raghuramjee - 121910313004

# Taking the inputs
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

# Logic implementation
if a >= b:
    lar = a
    sm = b
else:
    lar = b
    sm = a
dup = lar
while True:
    # checking to see if the larger is perfectly divisble by smaller
    if (dup % sm == 0):
        ans = dup
        break
    # increasing the factor of dup by 1 everytime
    dup += lar

# Printing the answer
print("The LCM of both the numbers is " + str(ans))