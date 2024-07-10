# Get list of numbers from input
k = input("Enter numbers separated by space: ").split()

# Convert the strings in the list to integers
for i in range(len(k)):
    k[i] = int(k[i])

# Get the new number from the user
number = int(input("Enter a number: "))

# Count the occurrences of the number in the list
count = k.count(number)

# Find the indices of the number in the list
indices = []
for i in range(len(k)):
    if k[i] == number:
        indices.append(i)

# Print the results
print("Count:", count)
print("Indices:", indices)
