from math import *
def sum_sole(n):
    sum=0
    for i in range(1,n+1,2):
        sum+=i
    return sum

def sum_sochan(n):
    sum=0
    for i in range(0,n+1,2):
        sum+=i
    return sum

def tich_cacso( n):
    res =1
    for i in range(1,n+1):
        res*=i
    return res

def tich_cacso_3( n):
    res =1
    for i in range(1,n+1):
        if i%3==0:
            res*=i
    return res

def snt(n):
    if(n==0 or n==1):
        return False
    elif n>2 and n%2==0:
        return False
    else:
        for i in range(3,isqrt(n)):
            if n%i==0:
                return False
                break
    return True

if __name__ =='__main__':
    n = int(input('Nhập vào n : '))
    print(f'tổng các số lẻ <= {n} : {sum_sole(n)}')
    print(f'tổng các số chẵn <= {n} : {sum_sochan(n)}')
    print(f'tích các số từ 1 đến {n} : {tich_cacso(n)}')
    print(f'tích các số chia hết cho 3 <= {n} : {tich_cacso_3(n)}')

    sum=0
    for i in range(1,n+1):
        if(snt(i)):
            sum+=i
    print(f'tổng các số nguyên tố <= {n} : {sum}')
