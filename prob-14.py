#Project Euler Problem-14
#Author Tushar Gayan

def coll_conj(n):
    if n == 1:
        return 1
    elif n%2==0:
        return n/2
    else:
        return 3*n + 1

def chain(n):
    m = []
    while n >= 1:
        m.append(coll_conj(n))
    print(m)
    return len(m)

list_num = []

def chain_len(n):
    i = n
    coll_list = []
    while coll_conj(n)>1:
        coll_list.append(coll_conj(n))
        i = coll_conj(n)
        print(coll_conj(i))
    return len(coll_list)

print(chain_len(13))
