#khái niệm
'''
- là 1 cấu trúc data cơ bản trong python , thuộc nhóm sequence
- gồm nhiều phần tử , mỗi phần tử có 1 vị trí từ 0 -> len(list)-1
- các phần tử có thể có kiểu data khác nhau 
- có thể truy cập bằng chỉ số âm từ -1-> -len-1 (truy cập ngược mảng list[-1] = list[len(list)-1])
'''

# cách khởi tạo
'''
+ ten_list = []
or 
+ tên_list = [ptu_1, ptu_2, ....]
'''

# truy cập theo vị trí
# ten_list[1] - truy cập vào vị trí 0> len(str)-1

#function
'''
+ len(list) - đếm số phần tử của list
+ sum(list) - tính tổng giá trị các phần tử
+ max(list) - tìm phần tử max trong list
+ min(list) - tìm phần tử min trong list
+ list.count(a) - đếm số lần xuất hiện của a trong list

+ ghép 2 list = dấu +   (list3 = list1 + list2)
+ mở rộng list1 với lit2 : list1.extend(list2) - nó giống cái + ở trên

+ tạo list bằng cách * list với số lượng : list4 = list1*4  - list4 = 4 lần list 1

+ check 1 phần tử có nằm trong list:  a in list1
+ tìm vị trí đầu tiên của 1 phần tử từ vị trí:  list1.index(a,i) - nếu k có i ta mặc định từ vị trí 0  
+ list.sort() - sắp xếp tăng
+ list.sort(reverse =  True) - sắp xếp giảm
+ list.reverse() - đảo ngược mảng

+ list.append(a) - thêm a vào cuối list
+ list.insert(a,idx) -chèn a vào vị trí idx

+ list[1] = 30 - gán lại giá trị

'''


# xóa theo vị trí
'''
del(list[idx]) - xóa phần tử tại vị trí idx
del(list[start,end]) - xóa từ vị trí start -> end-1

# xóa theo giá trị
list.remove(value) - xóa nếu phần tử value đầu tiên ---- nếu k tồn tại -> lỗi valueError

# xóa tất cả : list.clear()

# xóa list, biến khỏi vùng nhớ
del(list)

#lấy phần tử ra khỏi list - lấy ra rồi xóa luôn
list.pop(0) - lấy phần tử đầu tiên
list.pop() - lấy phần tử cuối cùng 
'''

#test
'''
list = [1,2,3,4,5,6,7,8,9]
list1 = list[0:5] #start -> end-1 
list2 = list[3:] # cắt từ vị trí start đến cuối
list3 = list[:2]  # cắt từ vị trí 0 đến end-1
print(list1) #[1, 2, 3, 4, 5]
print(list2) #[4, 5, 6, 7, 8, 9]
print(list3) [1, 2]
'''


# n = int(input('Nhập vào số phần tử : '))
# list =[]
# for i in range(0,n,1):
#     x = int(input(f'nhập vào phần tử {i+1} : '))
#     list.append(x)
list = list(eval(input('Nhập vào list số nguyên : '))) # ép về list luôn
print(list)
print(sum(list))