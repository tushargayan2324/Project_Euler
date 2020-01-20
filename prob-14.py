#Project Euler Problem-14
#Author Tushar Gayan

def coll_conj(n):
    if n == 1:
        return 1
    elif n%2==0:
        return n/2
    elif n%2!=0:
        return 3*n + 1

def coll_chain(n):
    num = n
    chain_list = []
    while num>1:
        #print(num)
        num = coll_conj(num)
        chain_list.append(num)
    return len(chain_list)+1

i = 1
num_1 = 1
num_2 = 0

for i in range(1000001):
    num_1 = coll_chain(i)
    if num_1 > num_2:
        num_2 = num_1
        c = i
    num_1+=1
    print(num_2,i,c)

print(num_2)
