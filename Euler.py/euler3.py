

import math


def prime_check(num):
    is_prime = True

    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            is_prime = False
            continue
    return is_prime

number = 600851475143

biggest_prime = 1

for i in range(2,int(math.sqrt(number))):
    if number % i == 0 and prime_check(i):
        biggest_prime = i

print(biggest_prime)

















































