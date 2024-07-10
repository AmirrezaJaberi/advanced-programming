# Function to get and print names that start with 'a' or 'A'
def get_and_print_a_names():
    names = []
    a_names = []

    # Get 10 names from input
    for i in range(10):
        name = input("Enter a name: ")
        names.append(name)

    # Place names that start with 'a' or 'A' in the a_names list
    for name in names:
        if name.lower().startswith("a"):
            a_names.append(name)

    # Print names
    print("Names that start with 'a' or 'A':")
    for a_name in a_names:
        print(a_name)


# Execute the function
get_and_print_a_names()
