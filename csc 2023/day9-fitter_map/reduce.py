# cơ chế hoạt động
'''
listN = [1,2,3,4]
ban đầu bắt x=1, y=2
=> sau đó x=3,y=3 (x là tổng của 1+2)
'''

from functools import reduce
listN = [1,2,3,4]
tong=reduce(lambda x,y:x+y,listN)
print(tong)

