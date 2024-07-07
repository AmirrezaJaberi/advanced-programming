## Practice 2 :
# Write a program that takes an input number and determines if it is even or odd.

# Input: Get a number from user input
number = int(input('Enter a number: '))

# Check if the number is even or odd
if number % 2 == 0:
    print('The number', number, 'is even.')
else:
    print('The number', number, 'is odd.')
