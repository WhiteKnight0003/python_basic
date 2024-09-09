#  giống kiểu cắt 1 mảng phần tử

#cú pháp : List[start: stop: step] với chỉ số k âm
'''
- với toán tử : bạn có thể xác định chỉ số bắt đầu , kết thúc , bước nhảy của các phần tử mà bạn muốn cắt ra trong list
- giá trij trả về : 1 list chứa các phần tử trong list bắt đầu từ start , kết thúc tại stop -1 với bước nhảy là step , 
nếu k có step thì mặc  định nó là 1
nếu k có start thì nó mặc định cắt từ vị trí 0
nếu k có end thì nó cắt đến cuối list
nếu start <0 và end quá lớn thì start =0 và end = len(list)


a = [10,20,30,40,50]
b = a[2 : 5 : 1]  # cắt từ vị trí 2 -> 5-1=4 với bước nhảy giữa các phần tử là 1
print(b)

'''


# lật ngược nhanh 1 list - dùng reverse or
# a = [2,3,4,5,2,1]
# b = a[::-1]
# print(b) # -> [1, 2, 5, 4, 3, 2]


# thay đổi giá trị của nhiều phần tử trong 1 đoạn 
a = [2,3,4,5,2,1]
a[2:5] = [100,200] # từ 2 -> 4   => [2, 3, 100, 200, 1] thay giá trị đoạn 2<= <= 4
print(a) # -> [1, 2, 5, 4, 3, 2]


# chèn nhanh vào đầu or cuối or giữa
'''
a = ['x','y', 'z'] 
a[:0] = [10,20,30] 
print(a) => [10,20,30,'x','y','z']


a = ['x','y', 'z'] 
a[len(a):] = [10,20,30] 
print(a) => ['x','y','z',10,20,30]


a = ['x','y', 'z'] 
a[1:1] = [10,20,30] 
print(a) => ['x',10,20,30,'y','z']
'''


#deep copy - giống như copy bình thường
a = ['x','y', 'z'] 
b = a[:]