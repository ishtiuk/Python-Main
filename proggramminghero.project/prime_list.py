def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_list(number):
    primes = []
  
    for i in range(2, number+1):
        if is_prime(i) is True:
            primes.append(i)

    return primes

print(prime_list(int(input("Enter your number: "))))