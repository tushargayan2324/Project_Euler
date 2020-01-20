#Project Euler Problem-47
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

def prime_factors_list(n):
    factors_list = []
    for i in xrange(2,n+1):
            if n%i == 0:
                if prime_check(i) == True:
                    factors_list.append(i)
    return set(factors_list)

i = 644
#while prime_factors_list(i).isdisjoint(prime_factors_list(i+1))==True and prime_factors_list(i+1).isdisjoint(prime_factors_list(i+2))==True and prime_factors_list(i+2).isdisjoint(prime_factors_list(i+3))==True:
#   print(i)
#   i += 1

print(i)

print(prime_factors_list(200))
