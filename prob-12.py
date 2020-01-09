#Project Euler Problem-12
#Author Tushar Gayan

def factors_list(n):
    list = []
    for i in xrange(1,int(math.sqrt(n))):
            if n%i == 0:
                    list.append(n);list.append(n/i)
    return list

def traiangle_nums(n):
    return (n)(n+1)/2

i = i+1
while len(factors_list(triangle_nums())) < 500:
    print triangle_nums(i), 
