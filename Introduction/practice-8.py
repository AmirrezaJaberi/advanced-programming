## Practice 8 :
# Program to continuously sum numbers entered by the user until a negative number is entered

total = 0
number = 0

while number >= 0:
    number = int(input("Enter a number (negative to exit): "))
    if number >= 0:
        total += number

print(f"The sum of the numbers entered is: {total}")
