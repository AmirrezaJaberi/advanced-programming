# Arithmetic Operators
a = 10
b = 5
print(a + b)  # 15
print(a - b)  # 5
print(a * b)  # 50
print(a / b)  # 2.0
print(a % b)  # 0
print(a**b)  # 100000
print(a // b)  # 2

# Comparison Operators
print(a == b)  # False
print(a != b)  # True
print(a > b)  # True
print(a < b)  # False
print(a >= b)  # True
print(a <= b)  # False

# Logical Operators
print(a > 5 and b < 10)  # True
print(a > 5 or b > 10)  # True
print(not (a > 5))  # False

# Assignment Operators
c = 10
c += 5 # c = c + 5
print(c)  # 15

# Membership Operators
list_numbers = [1, 2, 3, 4, 5]
print(3 in list_numbers)  # True
print(6 not in list_numbers)  # True

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # False
print(x is not y)  # True
