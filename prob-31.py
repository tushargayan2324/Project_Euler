#Project Euler Problem-31
#Author Tushar Gayan

##########################################
# Multinomial Theorem
##########################################

def mod_list(pow,terms):
    m = []
    for i in range(terms):
            if i%pow == 0:
                    m.append(1)
            else:
                    m.append(0)
    return m

import numpy as np

p = np.poly1d([1 for i in range(201)]) #1 pence

q = np.poly1d(mod_list(2,201)) #2 pence

r = np.poly1d(mod_list(5,201)) #5 pence

s = np.poly1d(mod_list(10,201)) #10 pence

t = np.poly1d(mod_list(20,201)) #20 pence

u = np.poly1d(mod_list(50,201)) #50 pence

v = np.poly1d(mod_list(100,201)) #100 pence

w = np.poly1d(mod_list(200,201)) #200 pence

m = p*q*r*s*t*u*v*w

print(m[200])
