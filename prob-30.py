#Project Euler Problem-30
#Author Tushar Gayan

def pow_sum(n):
    m = str(n)
    s = 0
    for i in m:
        #print(i)
        s += (int(i))**5
        #print(s)
    if n == s:
        return True

req_sum = 0

for i in range(2,(9**5)*5+1):
    if pow_sum(i)==True:
        req_sum += i

print(req_sum)
