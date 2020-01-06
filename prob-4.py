#Project Euler Problem-4
#Author Tushar Gayan

def is_palindrome(n):
    num = str(n)
    if num == num[::-1]:
            return True
    else:
            return False
m = []
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
            m.append(str(i*j))

n = []
for item in m:
    if is_palindrome(item)==True:
            n.append(int(item))

