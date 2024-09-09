#eval : nhập số kiểu nào trả về số kiểu đó
k1 = eval('2+3+5') # int
k2 = eval('25') #int 
k3 = eval('1.75') # float
k4 = eval('20,30,45')  #tuple
k5 = eval('[12,23,14,15]') # list

k = eval('abc') # lỗi: NameError - nó sẽ hiểu đây là 1 biến chưa đc khai báo


print()