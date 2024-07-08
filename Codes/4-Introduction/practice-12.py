## Practice 12 :
# Prime Number 10 to 1000

def is_prime(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
    return True

# Print prime numbers between 10 and 1000
print("Prime numbers between 10 and 1000:")
for num in range(10, 1001):
    if is_prime(num):
        print(num)
