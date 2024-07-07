## Practice 10 :
# Prime Number Counter

def is_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
    return True


count = 0  # Initialize counter for prime numbers
for i in range(10):  # Loop 10 times
    number = int(input("Enter a number: "))  # Input a number from user
    if is_prime(number):  # Check if the number is prime
        count += 1  # Increment count if prime

print(count)  # Output the count of prime numbers entered
