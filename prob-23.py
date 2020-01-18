#Project Euler Problem-23
#Author Tushar Gayan

import math,time

'''def factors_list_sum(n):
    factors_list = []
    if int(math.sqrt(n))**2 == n:
        for i in xrange(2,1+int(math.sqrt(n))):
            if n%i == 0:
                    factors_list.append(i);factors_list.append(n/i)
        factors_list.append(1)
    else:
        for i in xrange(2,1+int(math.sqrt(n))):
                if n%i == 0:
                        factors_list.append(i);factors_list.append(n/i)
        factors_list.append(1)
    return sum(factors_list)'''

def factors_list_sum(n):
    factors_list = []
    for i in xrange(1,1+int(math.sqrt(n))):
            if n%i == 0:
                    factors_list.append(i);factors_list.append(n/i)
    factors_list.remove(n)
    return sum(set(factors_list))

i = 1
list_num = []

start_time = time.time()

while i<int(28124):
    if factors_list_sum(i) > i:
        #print(i)
        list_num.append(i)
    i+=1
#print(len(list_num))
comp_num = []

for a in list_num:
    for b in list_num:
        if a+b<28124:
            comp_num.append(a+b)
            #print(a+b, a, b)

req_list = []
for i in range(1,28124):
    req_list.append(i)

n = set(req_list) - set(comp_num)
m = sum(set(n))

stop_time = time.time()
print(m,stop_time-start_time)

