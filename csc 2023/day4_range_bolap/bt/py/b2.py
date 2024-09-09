from math import *


def snt(n):
    if(n==0 or n==1):
        return False
    elif n%2==0 and n>2:
        return False
    else:
        for i in range(3,isqrt(n)):
            if n%i==0:
                return False
                break 
    return True    

if __name__ =='__main__':
    for i in range(1,20):
        if(snt(i)):
            print(i)