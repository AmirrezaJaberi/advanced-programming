## Practice 10 :
# Program to calculate (!a + !b) / !c

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Input values for !a, !b, and !c
a = int(input("Enter a value for !a: "))
b = int(input("Enter a value for !b: "))
c = int(input("Enter a value for !c: "))

# Calculate !a, !b, and !c using factorial function
not_a = factorial(a)
not_b = factorial(b)
not_c = factorial(c)

# Calculate (!a + !b) / !c
result = (not_a + not_b) / not_c

# Print the result
print(f"The result of (!{a} + !{b}) / !{c} is: {result}")
