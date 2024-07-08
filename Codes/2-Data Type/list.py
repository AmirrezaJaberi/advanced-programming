# list: Convert a range to a list
range_to_list = list(range(5))
print(range_to_list)  # Output: [0, 1, 2, 3, 4]

# First, define a list
my_list = [1, 2, 3, 4, 5]

# Adding an element to the list using append
my_list.append(6)
print("After appending 6:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Removing an element from the list
my_list.remove(3)
print("After removing 3:", my_list)  # Output: [1, 2, 4, 5, 6]

# Replacing an element in the list
my_list[2] = 10  # Replace the value 4 with 10
print("After replacing 4 with 10:", my_list)  # Output: [1, 2, 10, 5, 6]
