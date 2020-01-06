#Project Euler Problem-6
#Author Tushar Gayan

import sys

def main(n):
    integers = [i for i in range(1,1+n)]
    sq_int = [i**2 for i in range(1,1+n)]
    ans = (sum(integers))**2 - sum(sq_int)
    print ans

main(100)

# NOT REALLY A GOOD CODE

# IF THE NUMBER IS LARGE MEMORY ERROR BOUND TO OCCUR 
