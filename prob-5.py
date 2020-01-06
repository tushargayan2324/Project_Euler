#Project Euler Problem-5
#Author Tushar Gayan

'''import sys

def check(num):
    base = 1
    for i in range(1,len(sys.argv)):
        if num%int(sys.argv[i]) == 0:
            base = base*1
        else:
            base = base*0
    return base

def lcm(*args):
    m = [int(i) for i in args]
    lcm = min(m)
    while(check(lcm) != 1):
        lcm += 1
    print lcm'''

# THE ABOVE CODE IS INCOMPLETE.....

##########################################
#USING ASSOCIATIVE PROPERTY OF LCM
##########################################

import sys

def lcm(a,b):
    if a>b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def gen_lcm(*args):
    m = [i for i in args]
    var = args[0]
    for i in range(len(args)-1):
        req_lcm = lcm(var,int(m[i+1]))
        var = req_lcm
    print var
    return var

gen_lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

#THE CODE IS DAMN SLOW

##########################################
#ALSO CAN USE THE POWER METHOD
##########################################


