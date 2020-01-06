#Project Euler Problem-25
#Author Tushar Gayan


def fib(n):
    i=0
    a=0
    b=1
    while len(str(a))<n: 
        a,b = b, a+b
        i+=1
        print(a,i)

fib(1000)
