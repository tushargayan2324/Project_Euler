#Project Euler Problem-7
#Author Tushar Gayan

import sys,math

def prime_check(num):
    if num > 1:
            for i in xrange(2,int(math.sqrt(num)+1)):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

def nth_prime(n):
    m = []
    i = 2
    while n != len(m):
        if prime_check(i)==True:
            m.append(i)
        i += 1
    print max(m)

nth_prime(int(sys.argv[1]))
