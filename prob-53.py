#Project Euler Problem-53
#Author Tushar Gayan

from math import factorial

def C(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

i = 0

for n in range(23,101):
    for r in range(1,n+1):
        if C(n,r)>1000000:
            i+=1

print(i)
