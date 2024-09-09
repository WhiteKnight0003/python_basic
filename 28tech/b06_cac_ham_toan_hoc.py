from math import *
# hoặc from math import *

# print(help(math))  #in ra tất cả các hàm và mô tả của chúng 

'''   
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586


    '''

# 1 số hàm cơ bản 
print(sqrt(360)) # căn bậc 2 trả về dưới dụng float
print(isqrt(360)) # căn bậc 2 nhưng chỉ trả về phần nguyên - integer - k làm tròn

print(pow(2,10)) # căn bậc 2 trả về dạng float
print(2**10) # căn bậc 2 trả về dạng int

print(ceil(2.3)) # = 3    -> trả về số int tiếp theo lớn hơn số thực nhập vào
print(ceil(2.0)) # = 2    -> với .0 thì trả về chính nó
 
print(floor(2.3)) # = 2 ->  trả về số int trước nó và nhỏ hơn số thực nhập vào
print(floor(2.0)) # = 2    -> với .0 thì trả về chính nó
 
print(factorial(10)) # giai thừa của 1 số

print(gcd(4,8)) # ucln

print(comb(10,2)) # tổ hợp chập 2 của 10 hay 10C2


print(perm(5)) # hoán vị
print(perm(5,3)) # chỉnh hợp chập 3 của 5  5K3

print(fabs(-100.77)) # trị tuyệt đối của số float
print(abs(-100)) # trị tuyệt đối của số int

print(round(203.44)) # làm tròn số

print(min(2,3,4,5)) # tìm số nhỏ nhất
print(max(2,3,4,5)) # tìm số lớn nhất