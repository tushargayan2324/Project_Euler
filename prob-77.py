#Project Euler Problem-77
#Author Tushar Gayan

#Multinomial Theorem
import math
import numpy as np

def mod_list(pow,terms):
    m = []
    for i in range(terms):
            if i%pow == 0:
                    m.append(1)
            else:
                    m.append(0)
    return m[::-1]

def prime_check(num):
    if num > 1:
            for i in xrange(2,int(math.sqrt(num)+1)):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

'''prime_list = []
i = 1
while len(prime_list)<200:
    if prime_check(i) == True:
        prime_list.append(i)
    i +=1

print(prime_list)

m = 1

for i in prime_list:
    m *= np.poly1d(mod_list(i,30))
    #print(i)

print(np.poly1d(m))

#for i in range(480):
#    print(m[i])

print(m.c)'''

def partition(n):
    if n<4:
        return 1
    else:
        prime_list = []
        for i in range(2,n+1):
            if prime_check(i)==True:
                prime_list.append(i)
        #print(prime_list)
        poly_list = []
        poly = 1
        for j in prime_list:
            #poly_list.append(np.poly1d(mod_list(j,n+1)))
            #print(np.poly1d(mod_list(j,n+1)))
            poly *= np.poly1d(mod_list(j,n+1))
        return poly[n]

i = 1
while partition(i) < 5000:
    i += 1

print partition(i), i

