#Project Euler Problem-22
#Author Tushar Gayan

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_dict = {}

for i in range(1,1+len(alpha)):
    alpha_dict[alpha[i-1]] = i

print(alpha_dict)

name_file = open('p022_names.txt','r')

name_list_1 = []

for i in name_file:
    name_list_1.append(i)

name_list = name_list_1[0].split(',')
name_list.sort()

sum_name = 0

for name in name_list:
    print(name)
    s =0
    for j in name:
        if not j == '"':
            s+=alpha_dict[j]
    s*= int(name_list.index(name)+1)
    sum_name +=s

print(sum_name)
