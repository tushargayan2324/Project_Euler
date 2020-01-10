#Project Euler Problem-12
#Author Tushar Gayan

import math
def factors_list(n):
    list = []
    for i in xrange(1,int(math.sqrt(n))):
            if n%i == 0:
                    list.append(i);list.append(n/i)
    return list

def triangle_num(n):
    return (n)*(n+1)/2

i = 1
while (len(factors_list(triangle_num(i))) < 501):
    #print triangle_num(i), i, len(factors_list(triangle_num(i)))
    i += 1

print triangle_num(i), i, len(factors_list(triangle_num(i)))
