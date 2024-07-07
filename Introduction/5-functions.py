# General structure of a function
def function_name(parameter1, parameter2, ...):
    # Function body (code block)
    # Perform operations, calculations, or logic
    return result  # Optional: Return statement

# Example of a built-in function
def do_something(param1, param2):
    print(f"Parameters: {param1} and {param2}")

# Example of a recursive function: calculating factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
