#Project Euler Problem-29
#Author Tushar Gayan

req_list = []

for a in range(2,101):
    for b in range(2,101):
        req_list.append(a**b)

print(len(set(req_list)))
