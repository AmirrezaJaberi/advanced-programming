## Practice 6 :
# Program to find the maximum of 10 numbers entered by the user

# Initialize max to 0 (assuming all numbers are positive)
max = 0

# Loop to read 10 numbers from the user
for i in range(0, 10):
    number = int(input("Enter number: "))
    if max < number:  # Check if current number is greater than max
        max = number  # Update max if current number is greater

# Print the maximum number
print(max)
