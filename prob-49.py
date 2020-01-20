#Project Euler Problem-49
#Author Tushar Gayan

import math

def prime_check(num):
    if num > 1:
            for i in xrange(2,int(math.sqrt(num)+1)):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True

def perm_check(num_1,num_2):
    num_list_1 = [int(i) for i in str(num_1)]
    num_list_2 = [int(i) for i in str(num_2)]
    num_list_1.sort();num_list_2.sort()
    if num_list_1 == num_list_2:
        return True

prime_list = []

for i in range(1000,15000):
    if prime_check(i) == True:
            prime_list.append(i)

AP_list = []

"""for i in prime_list:
    for j in prime_list:
        for k in prime_list:
            if i+k == 2*j:
                AP_list.append([i,j,k])
                print(i,j,k)
"""
print(len(prime_list))
for jump in range(1, int((len(prime_list))/2)):
    for i in range(1,int(len(prime_list)/jump)):
        try:
            if 2*prime_list[i + jump] == prime_list[i] + prime_list[i + 2*jump]:
                if perm_check(prime_list[i],prime_list[i+jump]) == True and perm_check(prime_list[i+jump],prime_list[i+2*jump]) == True:
                    AP_list.append((prime_list[i],prime_list[i+jump],prime_list[i+2*jump]))
                    print((prime_list[i],prime_list[i+jump],prime_list[i+2*jump]))
        except:
            break

print(set(AP_list))
