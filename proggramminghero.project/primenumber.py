def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input())
check_prime = prime_number(number)                             # it's very useful that call a function through a variable. 

if prime_number(number):
    print("the number is prime")

else:
    print("number is not prime")

# def all_primes(number):
#     primes = []
#     for i in range(2, number+1):
#         if prime_number(i) is True:
#             primes.append(i)
#     return primes

# print(all_primes(int(input())))