#Project Euler Problem-9
#Author Tushar Gayan

def check_Pythagorean_triplet(x,y,z):
    if x**2 + y**2 == z**2:
        return True
    else:
        return False

pyth_list = []

for i in range(1,1001):
    for j in range(1,1001):
        k = 1000 - (i + j)
        if check_Pythagorean_triplet(i,j,k)==True:
            print(i,j,k)

