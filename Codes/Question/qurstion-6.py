# Get two lists from input
list1 = input("Enter first list of numbers separated by space: ").split()
list2 = input("Enter second list of numbers separated by space: ").split()

# Convert the strings in the lists to integers
for i in range(len(list1)):
    list1[i] = int(list1[i])

for i in range(len(list2)):
    list2[i] = int(list2[i])

# Check for common elements
common_found = False

for num1 in list1:
    for num2 in list2:
        if num1 == num2:
            common_found = True
            break
    if common_found:
        break

# Print the result
if common_found:
    print("Yes, they have at least one common element.")
else:
    print("No, they do not have any common elements.")
