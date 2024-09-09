
from math import *
def chu_vi(bankinh):
    return pi*2*bankinh

def dien_tich(bankinh):
    #return pi*pow(bankinh,2) # 
    return pi* (bankinh**2)

if __name__ =='__main__':
    r = eval(input('Nhập vào bán kính : '))
    ChuVi = f'Chu vi của hình tròn là : {chu_vi(r):.2f}\n'
    DienTich = f'Diện Tích của hình tròn là : {dien_tich(r):.2f}\n'
    print(ChuVi,DienTich)