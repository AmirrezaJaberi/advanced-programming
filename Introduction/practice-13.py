## Practice 13 :
# Program to calculate and print the sum of factorials from 1 to num

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

total = 0
number = int(input("Enter a number: "))  # Input the number for calculation
for i in range(1, number + 1):
    total += factorial(i)

print(f"The sum of factorials from 1 to {number} is: {total}")
