#Project Euler Problem-10
#Author Tushar Gayan
import math

def prime_check(num):
    if num > 1:
            for i in xrange(2,int(math.sqrt(num)+1)):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

primes = []

for i in range(1,2000001):
    if prime_check(i) == True:
        print(i)
        primes.append(i)

print(sum(primes))
