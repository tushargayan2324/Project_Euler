#Project Euler Problem-13
#Author Tushar Gayan

file = open('prob-13.dat','r')
m = []
for i in file:
    m.append(int(i))
n = sum(m)
print(str(n)[0:10:1])
