#Project Euler Problem-52
#Author Tushar Gayan

def f(num_1,num_2): #Checks same digit
    num_list_1 = [int(i) for i in str(num_1)]
    num_list_2 = [int(i) for i in str(num_2)]
    num_list_1.sort();num_list_2.sort()
    if num_list_1 == num_list_2:
        return True
    else:
        return False

n = 1

while f(n,2*n) != True or f(2*n,3*n) != True or f(3*n,4*n) != True or f(4*n,5*n) != True or f(5*n,6*n) != True:
    n+=1

print(n)
