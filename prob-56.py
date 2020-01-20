#Project Euler Problem-56
#Author Tushar Gayan

num_1 = 1
num_2 = 1

def digit_sum(n):
    s = 0
    for i in str(n):
        s+=int(i)
    return s

for a in range(1,100):
    for b in range(1,100):
        num_1 = a**b
        if digit_sum(num_1)>digit_sum(num_2):
            num_2 = num_1

print(digit_sum(num_2))
