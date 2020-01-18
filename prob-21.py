#Project Euler Problem-21
#Author Tushar Gayan

import math

def factors_list_sum(n):
    factors_list = []
    for i in xrange(2,int(math.sqrt(n))):
            if n%i == 0:
                    factors_list.append(i);factors_list.append(n/i)
    factors_list.append(1)
    return sum(factors_list)

i = 1
list_amicable_num = []

while i<4**10:
    n = factors_list_sum(i)
    if factors_list_sum(n) == i:
        if n != i:
            print(i)
            list_amicable_num.append(i)
    i+=1

print(sum(list_amicable_num))
