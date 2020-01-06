#Project Euler Problem-2
#Author Tushar Gayan

def fib(n):
    a,b = 1,1
    for i in xrange(n):
            a,b = b,a+b
    return b

m = 0
i = 0
while fib(i)<4000000:
    if fib(i)%2==0:
            m = m+fib(i)
    i = i + 1


