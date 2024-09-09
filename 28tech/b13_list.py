'''tính chaart của list 
- lists are ordered : CÁc phần tử trong list là có thứ tự 
- accessed by index : Truy cập các phần tử trong list thông qua chỉ số
- lists can contain any sort of object : có thể chứa các onject thuộc các kiểu dữ liệu khác nhau như int , float ,... hay là 1 list khác - kiểu lẫn lộn
- list are changeable(mutable) : các phần tử trong list có thể thay đổi giá trị , các thao tác them , xóa các phần tử cũng đc hỗ trợ'''


#  truy cập theo vị trí
#  a = [1,2,3,4] hay a = [1,2,3, '28tech', 5.6,....]
# 


# constructer - dùng cho cái gì có thể duyệt đc - như iterable
'''
 s = '28tech'
 a = list(s)
 print(a)  ->  ['2','8','t','e','c','h']


 a = list(100) - không thể vì 100 là số chứ k phải thứ có thể duyệt thứ tự

 a= range(20)  - range là 1 bộ lặp nên duyệt đcs
 print(a) -> 0<=a<=19 
'''



# len(a) : đếm số lượng phần từ 

#pyhthon cho truy cập vào cả vị trí âm
# a = [1,2,3,4]
#      0 1 2 3 - index
#     -4 -3 -2 -1  - negative index - con cuối cùng là -1 và giảm đần về trước
#  duyệt quá thì vẫn sẽ bị lỗi



#  duyệt list 
''' c1 : duyệt qua chỉ số
 a = []
 for i in range(len(a)): duyệt từ đầu đến cuối
  ...
 for i in range(-1,len(a) *-1-1,-1): duyệt từ cuối về đầu 
'''

'''c2 : duyệt bằng for each
a = []
for item in a:
   ...
'''



# thay đổi giá trị phần tử
# vd a = [] 
# a[-1] = 1  ,  a[2] = 3 ....

# thêm phần tử 
'''
append() : thêm 1 phần tử vào cuối list
a.append('ddd')


insert() : thêm 1 phần tử vào vị trí bất kỳ
a.insert(1, 'đâsdasd') - vị trí và cái muốn thêm - nếu vị trí thêm vào nằm ngoài kích thước nó sẽ tự động thêm vào cuối
'''


# xóa phần tử
'''
-  xóa qua vị trí
dùng pop() - nếu truyền vị trí vào nó sẽ xóa vị trí đó - k truyền vào thì xóa cuối - và nó có trả về phần tử bị xóa
dùng del a[vị trí] - xóa vị trí đó và k trả về phần tử bị xóa


- xóa qua giá trị
a.remove(giá trị) - nếu 1 list có nhiều giá trị đó nó sẽ xóa đi cái xuất hiện đầu tiên và phải đảm báo giá trị đó có tồn tại trong list nếu k tồn tại sẽ gây ra lỗi


- clear() - xóa tát cả phần tử
'''


#sao chép list - giúp nhân bản nội dung của 1 list ban đầu nhiều lần
''' 
a = [1,2,3]
b = a* 2 => b = [1,2,3,1,2,3]
'''


# tìm kiếm phần tử trong list - tìm kiếm tuyến tính - o(n)
'''
 a = [1,2,5,7,'fdf']
 if 5 in a:
   print('yes')
 ''' 

#combine list 
''' dùng hàm extend() để thêm 1 list khác vào list hiện tại (có thể dùng toán tử + cũng đc)
a.extend(b) or a+= b
'''


# copy tạo 1 list mới giống list ban đầu nhưng k phải list ban đầus
'''
c = a.copy()
'''


# phương thức của list
''' 
- a.count(x) - đếm số lần x xuất hiện - nhưng x phải có mặt trong mảng
- a.index(X) - trả về vị trí đầu tiên mà x xuất hiện - - nhưng x phải có mặt trong mảng
- a.reverse() - lật ngược 1 mảng
- a.sort() - sắp xếp mảng a 
- a.all() - trả về true nếu all phần tử trong list là true
- a.any() - trả về true nếu có ít nhất 1 phần tử trong list là true 
- a.max() - trả về phần tử lớn nhất trong list
- a.min() - trả về phần tử nhỏ nhất trong list
- a.sum() - tính tổng các phần tử trong list
'''