from math import *
def ucln(a, b):
    if b==0:
        return a
    return ucln(b,a%b)

if __name__ == '__main__':
    print('-'*20)
    print(f'{ucln(10,5)}'.center(20))# căn lề vào giữa 
    print('-'*20)
