#Project Euler Problem-3
#Author Tushar Gayan
import sys,math
factors_list = []

def factors(n):
    for i in xrange(1,int(math.sqrt(n))):
            if n%i == 0:
                    print i , n/i
                    factors_list.append(i);factors_list.append(n/i)
factors(int(sys.argv[1]))
def prime_check(num):
    if num > 1:
            for i in xrange(2,int(math.sqrt(num)+1)):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

prime_factors = []

for item in factors_list:
    if prime_check(item) == True:
        prime_factors.append(item)

print(max(prime_factors))
