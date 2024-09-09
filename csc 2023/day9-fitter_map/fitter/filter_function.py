from math import isqrt


def KTsnt(n):
    if n<=1: 
        return False
    elif n>2 and n%2==0:
        return False
    for i in range(3,isqrt(n)+1):
        if n%i==0:
            return False
    return True

if __name__ =="__main__":
    listN= [5,6,7,3,5,12,44,8,11,9]
    listSNT = list(filter(KTsnt,listN))
    print(listSNT)