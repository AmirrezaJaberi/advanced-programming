## Practice 1 :
# Write a program that reads two numbers from input and prints the larger number.

# Input: Get two numbers from user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Compare the two numbers and print the larger one
if number1 > number2:
    print("The larger number is:", number1)
elif number2 > number1:
    print("The larger number is:", number2)
else:
    print("Both numbers are equal.")
