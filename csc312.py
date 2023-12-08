def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_factors_stack(n):
    factors_stack = []

    # Find prime factors
    for i in range(2, n + 1):
        while is_prime(i) and n % i == 0:
            factors_stack.append(i)
            n //= i

    # Print prime factors in descending order
    print("Prime factors in descending order:")
    while factors_stack:
        print(factors_stack.pop(), end=" ")

# Input: positive integer
num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    prime_factors_stack(num)
