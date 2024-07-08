## Practice 7 :
# Program to print the factors of a number entered by the user

# Take input from the user
number = int(input("Enter a number: "))

# Print message if the number is less than or equal to zero
if number <= 0:
    print("Please enter a positive integer.")
else:
    print(f"The factors of {number} are:")

    # Find and print all factors of the number
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
