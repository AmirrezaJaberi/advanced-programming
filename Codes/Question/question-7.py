def has_zero(n):
    # Convert the number to string and check for '0'
    if "0" in str(n):
        return "The number contains zero."
    else:
        return "The number does not contain zero."


# Get the number from the user
number = int(input("Enter a number: "))
print(has_zero(number))
