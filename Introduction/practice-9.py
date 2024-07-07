## Practice 9 :
# Write a program to read !a, !b, and !c from input and calculate the following expression. ((!a+!b)/!c)

# Input values for variables a, b, and c
a = int(input("Enter a number: "))  # Get value for a
b = int(input("Enter b number: "))  # Get value for b
c = int(input("Enter c number: "))  # Get value for c

# Initialize variables for factorial calculations
d, e, f = 1, 1, 1

# Calculate factorial of a
for i in range(1, a + 1):
    d = d * i

# Calculate factorial of b
for i in range(1, b + 1):
    e = e * i

# Calculate factorial of c
for i in range(1, c + 1):
    f = f * i

# Calculate and print the result of (a+b)/c
print((a + b) / c)
