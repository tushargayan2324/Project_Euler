#Project Euler Problem-69
#Author Tushar Gayan

def phi(n):
    num_list = []
    for i in range(1,n+1):
        if n%i != 0:
            num_list.append(i)
    print(num_list)

req_num = 1
num = 1

'''for i in range(2,1000000+1):
    if phi(i)!=0:
        if float(i)/phi(i) > req_num:
            req_num = float(i)/phi(i)
            num = i
    print(num, req_num,i)
'''

print(num, req_num)

print(phi(6))

#INCOMPLETE CODE
