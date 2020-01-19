#Project Euler Problem-78
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

def partition(n):
    num_list = []
    for i in range(1,n+1):
        num_list.append(i)
    #print(num_list)
    poly_list = []
    poly = 1
    for j in num_list:
        #poly_list.append(np.poly1d(mod_list(j,n+1)))
        #print(np.poly1d(mod_list(j,n+1)))
        poly *= np.poly1d(mod_list(j,n+1))
    return poly[n]

i = 1
while partition(i)%1000000 != 0:
    i+=1
    print(partition(i),i)
